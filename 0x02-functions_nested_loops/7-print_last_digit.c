#include "main.h"

/**
 * print_last_digit - prints last digit in a number
 * @n: the int to extract the last digit
 * Return: value of the last digit
 */
int print_last_digit(int n)
{
	int m;

	if (n < 0)
		n = -n;

	m = n % 10;

	if (m < 0)
		m = -m;

	_putchar(m + '0');

	return (m);
}
