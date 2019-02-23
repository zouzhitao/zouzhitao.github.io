
> 以我面试多次大厂的经验，无论是笔试还是面试，大厂的算法题目都不会考非常难实现的数据结构或者算法模板，通常喜欢的还是偏思维的 hash, 复杂度，dp，这样一些简单算法

# 题目链接

[google kickstart 2018 Scrambled Words](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004)

# 分析

分析在题目网站有，首先需要想到的就是不同串的长度只有 $O(\sqrt{\sum words_i})$ 种，那么枚举所有长度肯定是一种可行的方法，不过呢，即使枚举长度，对于每个枚举到的字串，我们仍然需要将他和所有具有此长度的串比较，太过浪费时间了，怎么做才能加速呢？ 对 **hash**, 将dict中的串 hash 一下，那么查找时间就变成了$O(1)$, 所以最终的时间复杂度就变成了 $O(1)$

这里补充一些 hash 知识，其实这个在工业界用的非常多，所以基本上的程序语言都提供了丰富的类库，我用的是c++ 的unordered_map<>,当然，对于 个性化 的类还是需要自己写hash 函数以及 ==的，详见参考文献

# code

[github](https://github.com/zouzhitao/competitive-programing/blob/master/kick-start/Scrambled-Words.cpp)

# 参考文献

- [C++ unordered_map using a custom class type as the key](https://stackoverflow.com/questions/17016175/c-unordered-map-using-a-custom-class-type-as-the-key)
- [hash - c++ reference](https://en.cppreference.com/w/cpp/utility/hash)
- [unordered_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/?kw=unordered_map)



>**版权声明**
>
>本作品为作者原创文章，采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/) 
>
>**作者:** [taotao](https://zouzhitao.github.io/)
>
>**转载请保留此版权声明，并注明出处**



