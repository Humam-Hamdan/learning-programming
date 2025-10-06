def find_missing(A: list, n: int) -> int:
    result = 0

    for value in range(1, n + 1):
        result ^= value

    for value in A:
        result ^= value

    return result


def main() -> None:
    # something
    l = [1, 2, 3, 5]
    print(find_missing(l, 5))


if __name__ == "__main__":
    main()
