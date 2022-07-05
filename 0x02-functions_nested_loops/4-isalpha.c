#include "main.h"

/**
 *  _isalpha - check alphabetical letters
 *  @c: a charter to be checke on
 *  Return: returns 0 or 1 based on condition
 */
int _isalpha(int c)
{
	return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'));
}
