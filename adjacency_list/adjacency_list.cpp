// adjacency_list.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <list>

int main()
{
	std::ifstream fin("input.txt");
	int v_num, m_num = 0;
	fin >> v_num >> m_num;
	fin.get();
	std::vector<std::vector<int>> adjacency_list(v_num);
	for(int i = 0; i < m_num; i++)
	{
		int v_1, v_2 = 0;
		fin >> v_1 >> v_2;
		fin.get();
		adjacency_list[v_1 - 1].push_back(v_2);
		adjacency_list[v_2 - 1].push_back(v_1);
	}

	std::ofstream fout("output.txt");
	for (int i = 0; i < v_num; i++)
	{
		int adj_num = adjacency_list[i].size();
		fout << adj_num;
		for (int j = 0; j < adj_num; j++)
			fout << " " << adjacency_list[i][j];
		fout << std::endl;
	}
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
