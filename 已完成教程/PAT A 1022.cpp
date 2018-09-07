//#include<cstido>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct node {
  int id;
  string title, author, publish, year;
  vector<string> key;
};
vector<node> vec;
map<string, vector<int> > titles, authors, publishs, years, keys;

int n, m;

vector<string> change(string &str) {
  string temp;
  vector<string> mmp;
  for (int i = 0; i < str.size(); ++i) {
    if (str[i] != ' ') {
      temp.push_back(str[i]);
    } else {
      mmp.push_back(temp);
      temp.clear();
    }
  }
  if (temp.size()) {
    mmp.push_back(temp);
  }
  return mmp;
}

int main() {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    string waitchange;
    node temp;
    cin >> temp.id;
    getchar();
    getline(cin, temp.title);
    getline(cin, temp.author);
    getline(cin, waitchange);
    temp.key = change(waitchange);
    getline(cin, temp.publish);
    getline(cin, temp.year);
    vector<int> v;
    v.push_back(temp.id);
    vec.push_back(temp);

    if (titles.find(temp.tile) == titles.end())
      titles[temp.title] = v;
    else
      titles[temp.title].push_back(temp.id);
    if (authors.find(temp.author) == authors.end())
      authors[temp.author] = v;
    else
      authors[temp.author].push_back(temp.id);
    if (publishs.find(temp.publish) == publishs.end())
      publishs[temp.publish] = v;
    else
      publishs[temp.publish].push_back(temp.id);
    if (years.find(temp.year) == years.end())
      years[temp.year] = v;
    else
      years[temp.year].push_back(temp.id);
    for (int i = 0; i < temp.key.size(); ++i) {
      if (keys.find(temp.key[i]) == keys.end())
        keys[temp.key[i]] = v;
      else
        keys[temp.key[i]].push_back(temp.id);
    }
  }

  cin >> m;
  for (int i = 0; i < m; ++i) {
    int sign;
    cin >> sign;
    //		cout<<sign<<endl;
    getchar();
    getchar();
    string tempstr;
    getline(cin, tempstr);
    cout << sign << ": " << tempstr << endl;
    switch (sign) {
      case 1:
        if (titles.find(tempstr) == titles.end())
          cout << "Not Found" << endl;
        else {
          vector<int> tempint = titles[tempstr];
          sort(tempint.begin(), tempint.end());
          for (int i = 0; i < tempint.size(); ++i) {
            cout << tempint[i] << endl;
          }
        }
        break;
      case 2:
        if (authors.find(tempstr) == authors.end())
          cout << "Not Found" << endl;
        else {
          vector<int> tempint = authors[tempstr];
          sort(tempint.begin(), tempint.end());
          for (int i = 0; i < tempint.size(); ++i) {
            cout << tempint[i] << endl;
          }
        }
        break;
      case 3:
        if (keys.find(tempstr) == keys.end())
          cout << "Not Found" << endl;
        else {
          vector<int> tempint = keys[tempstr];
          sort(tempint.begin(), tempint.end());
          for (int i = 0; i < tempint.size(); ++i) {
            cout << tempint[i] << endl;
          }
        }
        break;
      case 4:
        if (publishs.find(tempstr) == publishs.end())
          cout << "Not Found" << endl;
        else {
          vector<int> tempint = publishs[tempstr];
          sort(tempint.begin(), tempint.end());
          for (int i = 0; i < tempint.size(); ++i) {
            cout << tempint[i] << endl;
          }
        }
        break;
      case 5:
        if (years.find(tempstr) == years.end())
          cout << "Not Found" << endl;
        else {
          vector<int> tempint = years[tempstr];
          sort(tempint.begin(), tempint.end());
          for (int i = 0; i < tempint.size(); ++i) {
            cout << tempint[i] << endl;
          }
        }
        break;
    }
  }
  return 0;
}
