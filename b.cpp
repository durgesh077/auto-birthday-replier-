#include <bits/stdc++.h>
using namespace std;
#define PTR template<typename T> void printer(T&con,int end=0,string sp=" ") \
{if constexpr(is_integral<T>::value){cout<<con<<sp;}else \
if constexpr(is_pointer<T>::value){fr(i,end){printer(*con,0,sp);con++;} \
cout<<endl;}else if constexpr(is_same<T,string>::value){cout<<con<<sp;}else \
if constexpr(is_same <T,pair<int,int>>::value or is_same <T,pair<char,int>>::value) \
{cout<<"("<<con.f<<","<<con.s<<")"<<sp;}else{for(auto&it:con)printer(it,0,sp); \
cout<<endl;}}struct PRINT{template<typename T>auto operator<<(T con){printer(con);return *this;} \
template<typename T>auto operator()(T con,int end=0,string sp=" ") \
{printer(con,end,sp);return *this;}}print
#define endl '\n'
#define ll long long
#define vi vector<int>
#define vvi vector < vi >
#define pii pair<int,int>
#define mod 1000000007
#define inf 0x3f3f3f3f
#define all(c) c.begin(),c.end()
#define mp(x,y) make_pair(x,y)
#define mem(a,val) memset(a,val,sizeof(a))
#define eb emplace_back
#define pb push_back
#define f first
#define s second
#define fr(x,to) for(int x=0;x<to;x++)
#define frg(x,to) for(int x=1;x<=to;x++)
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1001
set<int> adj[MAXN];
int par[MAXN],subSz[MAXN];
int dfs4size(int src,int parent)
{
	subSz[src]=0;
	for(auto &it:adj[src])
	{
		if(it!=src)
		subSz[src]+=dfs4size(it,src);
	}
	return subSz[src];
}
int dfs4centroid(int src,int par,int total_size)
{
	for(auto& it:adj[src])
		if(it!=par and subSz[it]>total_size/2)
			return dfs4centroid(it,src,total_size);

		return src;
}
void decompose(int src,int parent)
{
	dfs4size(src,parent);
	int centroid=dfs4centroid(src,parent,subSz[src]);
	par[centroid]=parent;
	for(auto&it:adj[centroid])
	{
		if(it==parent)
			continue;
		adj[it].erase(src);
		decompose(it,centroid);
	}
}
int main()
{
    //#ifndef ONLINE_JUDGE
    //freopen("C:\\Programs\\in.txt","r",stdin);
    ////freopen("C:\\Programs\\out.txt","w",stdout);
    //#endif
    //IOS;
    int T=1;
    cin>>T;
    while(T--)
    {
      int n,a,b;
      cin>>n;
      frg(i,n-1)
      cin>>a>>b,adj[a].insert(b),adj[b].insert(a);

      dfs4size(1,-1);
      decompose(1,-1);
      for(int i=1;i<=n;i++)
      	cout<<"parent["<<i<<"]= "<<par[i]<<endl;
    }
    return 0;
}
