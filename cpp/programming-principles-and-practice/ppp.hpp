// PPP.hpp
//
// Consolidated support header for
// "Programming: Principles and Practice using C++ (3rd edition)"
//
// Use this version on Linux with GCC/Clang, since standard modules
// (`import std;`) are not fully implemented yet.
//
// Compile with:
//    g++ -std=c++20 -Wall -Wextra prog.cpp -o prog
//

#pragma once

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <span>
#include <stdexcept>
#include <random>
#include <cstdint>
#include <list>
#include <map>
#include <unordered_map>
#include <set>
#include <memory>
#include <algorithm>

namespace PPP {

    using Unicode = long;

    // ------- checked containers ---------

    template <class T>
    concept Element = true;

    // Forward declaration for Checked_string
    class Checked_string;

    // trivially range-checked vector (no iterator checking)
    template <Element T>
    class Checked_vector : public std::vector<T> {
    public:
        using std::vector<T>::vector;

        T& operator[](size_t i) {
            std::cerr << "PPP::vector::[]\n";
            return this->std::vector<T>::at(i);
        }

        const T& operator[](size_t i) const {
            std::cerr << "PPP::vector::[] const\n";
            return this->std::vector<T>::at(i);
        }
    };

    class Checked_string : public std::string {
    public:
        using std::string::string;

        char& operator[](size_t i) {
            std::cerr << "PPP::string::[]\n";
            return this->std::string::at(i);
        }

        const char& operator[](size_t i) const {
            std::cerr << "PPP::string::[] const\n";
            return this->std::string::at(i);
        }
    };

    template <Element T>
    class Checked_span : public std::span<T> {
    public:
        using std::span<T>::span;

        T& operator[](size_t i) {
            std::cerr << "PPP::span::[]\n";
            if (i >= std::size(*this))
                throw std::runtime_error("span range error");
            return std::span<T>::operator[](i);
        }

        const T& operator[](size_t i) const {
            std::cerr << "PPP::span::[] const\n";
            if (i >= std::size(*this))
                throw std::runtime_error("span range error");
            return std::span<T>::operator[](i);
        }
    };

    // ------- error handling ---------

    struct Exit : std::runtime_error {
        Exit() : std::runtime_error("Exit") {}
    };

    inline void simple_error(std::string s) {
        std::cerr << "error: " << s << '\n';
        exit(1);
    }

    inline void error(const std::string& s) {
        throw std::runtime_error(s);
    }

    inline void error(const std::string& s, const std::string& s2) {
        error(s + s2);
    }

    inline void error(const std::string& s, int i) {
        std::ostringstream os;
        os << s << ": " << i;
        error(os.str());
    }

    enum class Error_action { ignore, throwing, terminating, logging, error };

    struct except_error : std::runtime_error {
        using runtime_error::runtime_error;
    };

    constexpr Error_action default_error_action = Error_action::error;

    template <Error_action action = default_error_action, typename C>
    constexpr void expect(C cond, std::string mess) {
        if constexpr (action == Error_action::logging)
            if (!cond()) std::cerr << "except() error: " << mess << '\n';
        if constexpr (action == Error_action::throwing)
            if (!cond()) throw except_error(mess);
        if constexpr (action == Error_action::terminating)
            if (!cond()) std::terminate();
        if constexpr (action == Error_action::error)
            if (!cond()) PPP::error(mess);
    }

    // ------- narrowing ---------

    template <class T, class U>
    constexpr T narrow_cast(U&& u) noexcept {
        return static_cast<T>(std::forward<U>(u));
    }

    struct narrowing_error : public std::exception {
        const char* what() const noexcept override {
            return "narrowing_error";
        }
    };

    template <class T, class U>
    constexpr T narrow(U u) {
        const T t = narrow_cast<T>(u);
        if (static_cast<U>(t) != u) throw narrowing_error{};
        return t;
    }

    // ------- random numbers ---------

    inline std::default_random_engine& get_rand() {
        static std::default_random_engine ran;
        return ran;
    }

    inline void seed(int s) { get_rand().seed(s); }
    inline void seed() { get_rand().seed(); }

    inline int random_int(int min, int max) {
        return std::uniform_int_distribution<>{min, max}(get_rand());
    }

    inline int random_int(int max) { return random_int(0, max); }

    template <typename C>
    using Value_type = typename C::value_type;

    template <typename C>
    using Iterator = typename C::iterator;

} // namespace PPP

// ---- make std::min() and std::max() available if macros exist
#undef min
#undef max

// ---- disgusting macro hacks to get range checking ----
using namespace PPP;
using namespace std;

#define vector Checked_vector
#define string Checked_string
#define span   Checked_span

// ---- enable hashing of Checked_string ----
// Temporarily disable the `string` macro so std::string isn't mangled here
#undef string
template <>
struct std::hash<PPP::Checked_string> {
    size_t operator()(const PPP::Checked_string& s) const noexcept {
        return std::hash<std::string>()(
            static_cast<const std::string&>(s));
    }
};
#define string Checked_string  // restore macro
