#include <iostream>
#include <iomanip>
using namespace std;

double CompTrapezoid(int n, double h, double f[]);
double CompSimpson(int n, double h, double f[]);
double CompMidpoint(int n, double a, double h, double f[]);

int main()
{
	double a, b;
	double h;
	int n;
	double f[100];
	cout << "Enter the lower limit of integration (a): ";
	cin >> a;
	cout << "Enter the upper limit of integration (b): ";
	cin >> b;
	cout << "Enter the change in x between each point (h): ";
	cin >> h;
	n = (b - a) / h;
	cout << "Enter the function values at each point: ";
	cout << "f(" << a << ") = ";
	cin >> f[0];
	for (int i = 1; i < n; i++)
	{
		cout << "f(" << a + i * h << ") = ";
		cin >> f[i];
	}
	cout << "f(" << b << ") = ";
	cin >> f[n];
	double resultTrap = CompTrapezoid(n, h, f);
	double resultSimp = CompSimpson(n, h, f);
	double resultMid = CompMidpoint(n, a, h, f);
	cout << "The result using the Composite Trapezoid is: " << setprecision(6) << resultTrap;
	cout << "\nThe result using Composite Simpson's Rule is " << setprecision(6) << resultSimp;
	cout << "\nThe result using Composite Midpoint Rule is " << setprecision(6) << resultMid;

}

double CompTrapezoid( int n, double h, double f[])
{
    double sum = 0.0;
    for (int i = 1; i < n; i++)
    {
        sum += 2 * f[i];
    }
    return (h / 2) * (f[0] + sum + f[n]);
}

double CompSimpson(int n, double h, double f[])
{
	double sum_odd = 0.0;
	double sum_even = 0.0;
	for (int i = 1; i < n; i++)
	{
		if (i % 2 == 0)
		{
			sum_even += f[i];
		}
		else
		{
			sum_odd += f[i];
		}
	}
	return (h / 3) * (f[0] + 4 * sum_odd + 2 * sum_even + f[n]);
}

double CompMidpoint(int n, double a, double h, double f[])
{
	double sum = 0.0;
	for (int i = 0; i < n / 2; i++)
	{
		sum += f[2 * i + 1];
	}
	return 2 * h * sum;
}