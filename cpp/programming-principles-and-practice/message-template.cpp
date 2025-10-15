#include "ppp.hpp"
using namespace std;

int main(){
	string first_name;
	cout << "Enter the name of the person you want to write a message to: \n";
	cin >> first_name;
	string friend_name;
	cout << "enter the name of the co-friend: \n";
	cin >> friend_name;
	int age = -1;
	cout << "enter the age of " << first_name <<  " \n";
	cin >> age;
	if (age <= 0 || age >= 110)
		simple_error("you're kidding!");
	cout << "Dear " << first_name << ",\n";
	cout << "	How are you? I am fine, we miss you. I heard you became " << age << " years old, congrats! ";
	if ( age < 12 )
		cout << "next year you will be " << age + 1;
	if ( age == 17)
		cout << "next year you can vote";
	if ( age >= 70)
		cout << "have you retired?";
	cout << " Have you seen " << friend_name << " lately?\n";
	cout << "Yours sincerely, \n" << '\n' << "Humam\n";
}
