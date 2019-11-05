
#include "pch.h"
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
	ifstream fin("minpath.in");
	ofstream fout("minpath.out");

	int n, m, start, finish;
	fin >> n >> m >> start >> finish;
	start--; finish--;

	vector < vector<pair<int, int>> > g(n);
	
	int a, b, weight;
	for (int i = 0; i < m; i++)
	{
		fin >> a >> b >> weight;
		g[--a].push_back(make_pair(--b, weight));
	}
	
	int* parents = new int[n];
	int* minpath = new int[n];

	for (int i = 0; i < n; i++)
	{
		minpath[i] = 1000000000;
	}
	bool* used = new bool[n] {false};

	minpath[start] = 0;
	for (int i = 0; i < n; ++i)
	{
		int v = -1;
		for (int j = 0; j < n; ++j)
		{
			if (!used[j])
			{
				if (v == -1 || minpath[j] < minpath[v])
					v = j;
			}
		}
		if (minpath[v] == 1000000000)
			break;

		used[v] = true;

		for (int j = 0; j < g[v].size(); ++j)
		{
			int to = g[v][j].first;
			int	length = g[v][j].second;
			if (minpath[v] + length < minpath[to]) 
			{
				minpath[to] = minpath[v] + length;
				parents[to] = v;
			}
		}
	}
	if (minpath[finish] == 1000000000)
		fout << 0;
	else
	{
		fout << minpath[finish] << endl;
		
		vector<int> path;
		for (int v = finish; v != start; v = parents[v])
		{
			path.push_back(v);
		}
		path.push_back(start);
		reverse(path.begin(), path.end());
		for (auto it : path)
			fout << ++it << " ";
		
	}
	return 0;
}
