
#include "pch.h"
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	ifstream fin("graph.in");
	ofstream fout("graph.out");
	int n, m;
	fin >> n >> m;
	//Вес ребра, начало ребра - конец ребра
	vector < pair < int, pair<int, int> > > g(m); 
	for(int i = 0; i < m; i++)
	{

		int weight, n1, n2;
		fin >> weight >> n1 >> n2;
		n1--;
		n2--;
		g[i].first = weight;
		g[i].second = make_pair(n1, n2);
	}
	int cost = 0;
	vector < pair<int, int> > core;

	sort(g.begin(), g.end());
	vector<int> tree_id(n);
	for (int i = 0; i < n; ++i)
		tree_id[i] = i;
	for (int i = 0; i < m; ++i)
	{
		int a = g[i].second.first, b = g[i].second.second, l = g[i].first;
		if (tree_id[a] != tree_id[b])
		{
			cost += l;
			core.emplace_back(a, b);
			int old_id = tree_id[b], new_id = tree_id[a];
			for (int j = 0; j < n; ++j)
				if (tree_id[j] == old_id)
					tree_id[j] = new_id;
		}
	}
	for(auto i = core.begin(); i != core.end(); ++i)
	{
		fout << i->first + 1 << " " << i->second + 1 << endl;
	}

	return 0;
}
