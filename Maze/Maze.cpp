

#include "pch.h"
#include <iostream>
#include <list>
#include <stack>
#include <fstream>
using namespace std;
int get_num(pair<int, int> room, int cols)
{
	int k = 0;
	k = (room.first - 1) * cols + room.second - 1;
	
	return k;
}
pair<int, int> get_pair(const int k, int cols)
{
	pair<int, int> p;
	p.first = (k / cols) + 1;
	p.second = (k % cols) + 1;
	return p;
}
int main()
{
	ifstream fin("maze.in");
	ofstream fout("maze.out");

	int rows, cols, x_start, y_start, x_finish, y_finish;
	fin >> rows >> cols >> x_start >> y_start >> x_finish >> y_finish;
	bool ** maze = new bool*[rows];
	for (int i = 0; i < rows; i++)
		maze[i] = new bool[cols];

	for (int i = 0; i < rows; i++)
		for (int j = 0; j < cols; j++)
			fin >> maze[i][j];

	list<pair<int, int>> que;
	que.push_back(make_pair(x_start, y_start));

	if (x_start == x_finish && y_start == y_finish)
	{
		fout << 0 << endl;
		fout << x_start << " " << y_start << endl;
		return 0;
	} 
	
	int *parents = new int[cols * rows];
	bool find = false;
	while (!que.empty())
	{
		pair<int, int> room = que.front();
		que.pop_front();
		if (room.first == x_finish && room.second == y_finish)
		{
			find = true;
			break;
		}

		int x = room.first - 1;
		int y = room.second - 1;
		

		//Комнаты, которые можно проверять, не выходя за пределы лабиринта
		bool left, up, right, down;
		left = up = right = down = true;
		if (y == 0)
			left = false;
		if (x == 0)
			up = false;
		if (y == cols - 1)
			right = false;
		if (x == rows - 1)
			down = false;

		//Проверка комнат
		if (left && maze[x][y - 1])
		{
			parents[x * cols + y - 1] = get_num(room, cols);
			maze[x][y - 1] = false;
			que.push_back(make_pair(x + 1, y));
		}
		if (up && maze[x - 1][y])
		{
			
			parents[(x - 1)*cols + y] = get_num(room, cols);
			maze[x - 1][y] = false;
			que.push_back(make_pair(x, y + 1));
		}
		if (right && maze[x][y + 1])
		{
			parents[x * cols + y + 1] = get_num(room, cols);
			maze[x][y + 1] = false;
			que.push_back(make_pair(x + 1, y + 2));
		}
		if (down && maze[x + 1][y])
		{
			parents[(x + 1) * cols + y] = get_num(room, cols);
			maze[x + 1][y] = false;
			que.push_back(make_pair(x + 2, y + 1));
		}

	}

	
	
	
	if (find)
	{
		stack<pair<int, int>> path;
		path.push(make_pair(x_finish, y_finish));
		

		int curr_num = get_num(make_pair(x_finish, y_finish), cols);
		while (true)
		{
			pair<int,int> room = get_pair(parents[curr_num], cols);
			path.push(room);
			if (room.first == x_start && room.second == y_start)
				break;
			curr_num = parents[curr_num];
		}
		fout << path.size() - 1 << endl;
		while (!path.empty())
		{
			pair<int,int> room = path.top();
			fout << room.first << " " << room.second << endl;
			path.pop();
		}
	}
	else
		fout << -1;

	return 0;
}