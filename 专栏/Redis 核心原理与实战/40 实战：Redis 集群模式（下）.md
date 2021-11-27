<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>40 实战：Redis 集群模式（下）.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="01&#32;Redis&#32;是如何执行的.md">01 Redis 是如何执行的.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;Redis&#32;快速搭建与使用.md">02 Redis 快速搭建与使用.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;Redis&#32;持久化——RDB.md">03 Redis 持久化——RDB.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;Redis&#32;持久化——AOF.md">04 Redis 持久化——AOF.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Redis&#32;持久化——混合持久化.md">05 Redis 持久化——混合持久化.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;字符串使用与内部实现原理.md">06 字符串使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;附录：更多字符串操作命令.md">07 附录：更多字符串操作命令.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;字典使用与内部实现原理.md">08 字典使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;附录：更多字典操作命令.md">09 附录：更多字典操作命令.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;列表使用与内部实现原理.md">10 列表使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;附录：更多列表操作命令.md">11 附录：更多列表操作命令.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;集合使用与内部实现原理.md">12 集合使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;附录：更多集合操作命令.md">13 附录：更多集合操作命令.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;有序集合使用与内部实现原理.md">14 有序集合使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;附录：更多有序集合操作命令.md">15 附录：更多有序集合操作命令.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Redis&#32;事务深入解析.md">16 Redis 事务深入解析.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;Redis&#32;键值过期操作.md">17 Redis 键值过期操作.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;Redis&#32;过期策略与源码分析.md">18 Redis 过期策略与源码分析.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Redis&#32;管道技术——Pipeline.md">19 Redis 管道技术——Pipeline.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;查询附近的人——GEO.md">20 查询附近的人——GEO.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;游标迭代器（过滤器）——Scan.md">21 游标迭代器（过滤器）——Scan.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;优秀的基数统计算法——HyperLogLog.md">22 优秀的基数统计算法——HyperLogLog.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;内存淘汰机制与算法.md">23 内存淘汰机制与算法.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;消息队列——发布订阅模式.md">24 消息队列——发布订阅模式.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;消息队列的其他实现方式.md">25 消息队列的其他实现方式.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;消息队列终极解决方案——Stream（上）.md">26 消息队列终极解决方案——Stream（上）.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;消息队列终极解决方案——Stream（下）.md">27 消息队列终极解决方案——Stream（下）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;实战：分布式锁详解与代码.md">28 实战：分布式锁详解与代码.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;实战：布隆过滤器安装与使用及原理分析.md">29 实战：布隆过滤器安装与使用及原理分析.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;完整案例：实现延迟队列的两种方法.md">30 完整案例：实现延迟队列的两种方法.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;实战：定时任务案例.md">31 实战：定时任务案例.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;实战：RediSearch&#32;高性能的全文搜索引擎.md">32 实战：RediSearch 高性能的全文搜索引擎.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;实战：Redis&#32;性能测试.md">33 实战：Redis 性能测试.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;实战：Redis&#32;慢查询.md">34 实战：Redis 慢查询.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;实战：Redis&#32;性能优化方案.md">35 实战：Redis 性能优化方案.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;实战：Redis&#32;主从同步.md">36 实战：Redis 主从同步.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;实战：Redis哨兵模式（上）.md">37 实战：Redis哨兵模式（上）.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;实战：Redis&#32;哨兵模式（下）.md">38 实战：Redis 哨兵模式（下）.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;实战：Redis&#32;集群模式（上）.md">39 实战：Redis 集群模式（上）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="40&#32;实战：Redis&#32;集群模式（下）.md">40 实战：Redis 集群模式（下）.md</a>
                    

                </li>
                <li>

                    
                    <a href="41&#32;案例：Redis&#32;问题汇总和相关解决方案.md">41 案例：Redis 问题汇总和相关解决方案.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;技能学习指南.md">42 技能学习指南.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;加餐：Redis&#32;的可视化管理工具.md">43 加餐：Redis 的可视化管理工具.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>40 实战：Redis 集群模式（下）</h1>
<p>上篇文章我们讲了 Redis 集群的搭建与节点的动态添加和删除，我们这里再来简单的复习一下，其中 30001~30006 是我们最初搭建的集群，而 30007 和 30008 是后面动态添加的主从节点，我们使用 <code>--cluster info</code> 命令来看一下主节点和槽位的分配情况，执行代码如下：</p>
<pre><code class="language-shell">$ redis-cli --cluster info 127.0.0.1:30001
127.0.0.1:30001 (887397e6...) -&gt; 0 keys | 5461 slots | 1 slaves.
127.0.0.1:30007 (df019085...) -&gt; 0 keys | 0 slots | 1 slaves.
127.0.0.1:30003 (f5958382...) -&gt; 0 keys | 5461 slots | 1 slaves.
127.0.0.1:30002 (3da35c40...) -&gt; 0 keys | 5462 slots | 1 slaves.
[OK] 0 keys in 4 masters.
0.00 keys per slot on average.

</code></pre>
<p>可以看出动态添加的主节点 30007 有一个从节点，但并没有分配任何槽位，这显然是不能满足我们的需求的，只添加了节点，但不处理任何数据，所以我们需要重新分片，让数据存储在所有的主节点上，这样才能发挥集群的最大作用。</p>
<h3>重新分片</h3>
<p>我们可以使用 reshard 命令，对槽位（slots）进行重新分配，执行命令如下：</p>
<pre><code class="language-shell">$ redis-cli --cluster reshard 127.0.0.1:30007
&gt;&gt;&gt; Performing Cluster Check (using node 127.0.0.1:30007)
M: df0190853a53d8e078205d0e2fa56046f20362a7 127.0.0.1:30007
   slots:[0-1332],[5461-6794],[10923-12255] (4000 slots) master
   1 additional replica(s)
S: dc0702625743c48c75ea935c87813c4060547cef 127.0.0.1:30006
   slots: (0 slots) slave
   replicates 3da35c40c43b457a113b539259f17e7ed616d13d
M: 3da35c40c43b457a113b539259f17e7ed616d13d 127.0.0.1:30002
   slots:[6795-10922] (4128 slots) master
   1 additional replica(s)
S: 1a324d828430f61be6eaca7eb2a90728dd5049de 127.0.0.1:30004
   slots: (0 slots) slave
   replicates f5958382af41d4e1f5b0217c1413fe19f390b55f
S: 1d09d26fd755298709efe60278457eaa09cefc26 127.0.0.1:30008
   slots: (0 slots) slave
   replicates df0190853a53d8e078205d0e2fa56046f20362a7
S: abec9f98f9c01208ba77346959bc35e8e274b6a3 127.0.0.1:30005
   slots: (0 slots) slave
   replicates 887397e6fefe8ad19ea7569e99f5eb8a803e3785
M: f5958382af41d4e1f5b0217c1413fe19f390b55f 127.0.0.1:30003
   slots:[12256-16383] (4128 slots) master
   1 additional replica(s)
M: 887397e6fefe8ad19ea7569e99f5eb8a803e3785 127.0.0.1:30001
   slots:[1333-5460] (4128 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
&gt;&gt;&gt; Check for open slots...
&gt;&gt;&gt; Check slots coverage...
[OK] All 16384 slots covered.
How many slots do you want to move (from 1 to 16384)?

</code></pre>
<p>在执行的过程中，它会询问你打算移动多少个节点，取值范围是 1 到 16384，我们这里输入 4000，意思是移动 4000 个槽位到某个主节点，输入命令之后，执行效果如下：</p>
<pre><code class="language-shell">How many slots do you want to move (from 1 to 16384)? 4000
What is the receiving node ID?

</code></pre>
<p>接着它会询问你需要把这些槽位分配到哪个节点上，请输入节点 Id，我们把上面 30007 端口的 Id 输入进去之后，敲击回车，执行效果如下：</p>
<pre><code class="language-shell">How many slots do you want to move (from 1 to 16384)? 4000
What is the receiving node ID? df0190853a53d8e078205d0e2fa56046f20362a7
Please enter all the source node IDs.
  Type 'all' to use all the nodes as source nodes for the hash slots.
  Type 'done' once you entered all the source nodes IDs.
Source node #1:

</code></pre>
<p>此时它会询问你要从那个源节点中进行转移，输入 <code>all</code> 命令表示从所有节点中随机抽取，执行效果如下：</p>
<pre><code class="language-shell"># ......忽略其他
Moving slot 2656 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2657 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2658 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2659 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2660 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2661 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2662 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2663 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2664 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Moving slot 2665 from 887397e6fefe8ad19ea7569e99f5eb8a803e3785
Do you want to proceed with the proposed reshard plan (yes/no)?

</code></pre>
<p>此时它会把所有要转移的节点信息列举出来，让你确认，你只需要输入 <code>yes</code> 就开始执行转移操作了。</p>
<p>在执行完转移之后，我们使用 <code>cluster slots</code> 命令来查看一下槽位的相关信息，结果如下：</p>
<pre><code class="language-shell">$ redis-cli -c -p 30001
127.0.0.1:30001&gt; cluster slots # 查看集群槽位信息
1) 1) (integer) 0
   2) (integer) 1332
   3) 1) &quot;127.0.0.1&quot;
      2) (integer) 30007
      3) &quot;df0190853a53d8e078205d0e2fa56046f20362a7&quot;
   4) 1) &quot;127.0.0.1&quot;
      2) (integer) 30008
      3) &quot;1d09d26fd755298709efe60278457eaa09cefc26&quot;
2) 1) (integer) 5461
   2) (integer) 6794
   3) 1) &quot;127.0.0.1&quot;
      2) (integer) 30007
      3) &quot;df0190853a53d8e078205d0e2fa56046f20362a7&quot;
   4) 1) &quot;127.0.0.1&quot;
      2) (integer) 30008
      3) &quot;1d09d26fd755298709efe60278457eaa09cefc26&quot;
3) 1) (integer) 10923
   2) (integer) 12255
   3) 1) &quot;127.0.0.1&quot;
      2) (integer) 30007
      3) &quot;df0190853a53d8e078205d0e2fa56046f20362a7&quot;
   4) 1) &quot;127.0.0.1&quot;
      2) (integer) 30008
      3) &quot;1d09d26fd755298709efe60278457eaa09cefc26&quot;
4) 1) (integer) 12256
   2) (integer) 16383
   3) 1) &quot;127.0.0.1&quot;
      2) (integer) 30003
      3) &quot;f5958382af41d4e1f5b0217c1413fe19f390b55f&quot;
   4) 1) &quot;127.0.0.1&quot;
      2) (integer) 30004
      3) &quot;1a324d828430f61be6eaca7eb2a90728dd5049de&quot;
5) 1) (integer) 6795
   2) (integer) 10922
   3) 1) &quot;127.0.0.1&quot;
      2) (integer) 30002
      3) &quot;3da35c40c43b457a113b539259f17e7ed616d13d&quot;
   4) 1) &quot;127.0.0.1&quot;
      2) (integer) 30006
      3) &quot;dc0702625743c48c75ea935c87813c4060547cef&quot;
6) 1) (integer) 1333
   2) (integer) 5460
   3) 1) &quot;127.0.0.1&quot;
      2) (integer) 30001
      3) &quot;887397e6fefe8ad19ea7569e99f5eb8a803e3785&quot;
   4) 1) &quot;127.0.0.1&quot;
      2) (integer) 30005
      3) &quot;abec9f98f9c01208ba77346959bc35e8e274b6a3&quot;

</code></pre>
<p>从结果可以看出 30007 分别从其他三个主节点中抽取了一部分槽位，作为了自己的槽位。</p>
<blockquote>
<p>注意，执行此过程中如果出现 <code>/usr/bin/env: ruby: No such file or directory</code> 错误，表明工具在执行的时候需要依赖 Ruby 环境，可使用命令 <code>yum install ruby</code> 安装 Ruby 环境即可。</p>
</blockquote>
<h3>槽位定位算法</h3>
<p>Redis 集群总共的槽位数是 16384 个，每一个主节点负责维护一部分槽以及槽所映射的键值数据，Redis 集群默认会对要存储的 key 值使用 CRC16 算法进行 hash 得到一个整数值，然后用这个整数值对 16384 进行取模来得到具体槽位，公式为：</p>
<blockquote>
<p>slot = CRC16(key) % 16383</p>
</blockquote>
<h3>负载均衡</h3>
<p>在 Redis 集群负载不均衡的情况下，我们可以使用 rebalance 命令重新分配各个节点负责的槽数量，从而使得各个节点的负载压力趋于平衡，从而提高 Redis 集群的整体运行效率。</p>
<p>rebalance 命令如下：</p>
<pre><code class="language-shell">$ redis-cli --cluster rebalance 127.0.0.1:30007

</code></pre>
<p>需要注意的是，即使输入 rebalance 命令，但它可能不会执行，当它认为没有必要进行分配时会直接退出，如下所示：</p>
<pre><code class="language-shell">$ redis-cli --cluster rebalance 127.0.0.1:30007
&gt;&gt;&gt; Performing Cluster Check (using node 127.0.0.1:30007)
[OK] All nodes agree about slots configuration.
&gt;&gt;&gt; Check for open slots...
&gt;&gt;&gt; Check slots coverage...
[OK] All 16384 slots covered.
*** No rebalancing needed! All nodes are within the 2.00% threshold.

</code></pre>
<h3>代码实战</h3>
<p>前面我们讲了 Redis 集群搭建的相关功能，接下来我们使用 Java 代码来操作一下 Redis 集群，本文依然使用 Jedis 来作为客户端进行相关的操作，核心代码如下：</p>
<pre><code class="language-java">import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;
import java.util.HashSet;
import java.util.Set;

public class ClusterExample {
    public static void main(String[] args) {
        // 集群节点信息
        Set&lt;HostAndPort&gt; nodes = new HashSet&lt;&gt;();
        nodes.add(new HostAndPort(&quot;127.0.0.1&quot;, 30001));
        nodes.add(new HostAndPort(&quot;127.0.0.1&quot;, 30002));
        nodes.add(new HostAndPort(&quot;127.0.0.1&quot;, 30003));
        nodes.add(new HostAndPort(&quot;127.0.0.1&quot;, 30004));
        nodes.add(new HostAndPort(&quot;127.0.0.1&quot;, 30005));
        nodes.add(new HostAndPort(&quot;127.0.0.1&quot;, 30006));
        // 创建集群连接
        JedisCluster jedisCluster = new JedisCluster(nodes,
                10000,  // 超时时间
                10);    // 最大尝试重连次数
        // 添加数据
        String setResult = jedisCluster.set(&quot;lang&quot;, &quot;redis&quot;);
        // 输出结果
        System.out.println(&quot;添加：&quot; + setResult);
        // 查询结果
        String getResult = jedisCluster.get(&quot;lang&quot;);
        // 输出结果
        System.out.println(&quot;查询：&quot; + getResult);
    }
}

</code></pre>
<p>以上程序的执行结果如下：</p>
<pre><code>添加：OK
查询：redis

</code></pre>
<p>此结果表明 Redis 集群操作正常，除了使用的操作对象不同之外，操作的方法名称都是相同的，所以对程序员来说比较友好，你可以根据自己的业务场景去写相应的代码了。</p>
<h3>故障</h3>
<p>在文章的最后部分，我们来看一下 Redis 集群故障相关的知识点，这样在我们遇到一些故障问题时就不会那么慌张了，并且能为我们处理故障时提供一些帮助。</p>
<h4><strong>故障发现</strong></h4>
<p>故障发现里面有两个重要的概念：疑似下线（PFAIL-Possibly Fail）和确定下线（Fail）。</p>
<p>集群中的健康监测是通过定期向集群中的其他节点发送 PING 信息来确认的，如果发送 PING 消息的节点在规定时间内，没有收到返回的 PONG 消息，那么对方节点就会被标记为疑似下线。</p>
<p>一个节点发现某个节点疑似下线，它会将这条信息向整个集群广播，其它节点就会收到这个消息，并且通过 PING 的方式监测某节点是否真的下线了。如果一个节点收到某个节点疑似下线的数量超过集群数量的一半以上，就可以标记该节点为确定下线状态，然后向整个集群广播，强迫其它节点也接收该节点已经下线的事实，并立即对该失联节点进行主从切换。</p>
<p>这就是疑似下线和确认下线的概念，这个概念和哨兵模式里面的主观下线和客观下线的概念比较类似。</p>
<h4><strong>故障转移</strong></h4>
<p>当一个节点被集群标识为确认下线之后就可以执行故障转移了，故障转移的执行流程如下：</p>
<ol>
<li>从下线的主节点的所有从节点中，选择一个从节点（选择的方法详见下面“新主节点选举原则”部分）；</li>
<li>从节点会执行 SLAVEOF NO ONE 命令，关闭这个从节点的复制功能，并从从节点转变回主节点，原来同步所得的数据集不会被丢弃；</li>
<li>新的主节点会撤销所有对已下线主节点的槽指派，并将这些槽全部指派给自己；</li>
<li>新的主节点向集群广播一条 PONG 消息，这条 PONG 消息是让集群中的其他节点知道此节点已经由从节点变成了主节点，并且这个主节点已经接管了原本由已下线节点负责处理的槽位信息；</li>
<li>新的主节点开始处理相关的命令请求，此故障转移过程完成。</li>
</ol>
<h4><strong>新主节点选举原则</strong></h4>
<p>新主节点选举的方法是这样的：</p>
<ol>
<li>集群的纪元（epoch）是一个自增计数器，初始值为0；</li>
<li>而每个主节点都有一次投票的机会，主节点会把这一票投给第一个要求投票的从节点；</li>
<li>当从节点发现自己正在复制的主节点确认下线之后，就会向集群广播一条消息，要求所有有投票权的主节点给此从节点投票；</li>
<li>如果有投票权的主节点还没有给其他人投票的情况下，它会向第一个要求投票的从节点发送一条消息，表示把这一票投给这个从节点；</li>
<li>当从节点收到投票数量大于集群数量的半数以上时，这个从节点就会当选为新的主节点。</li>
</ol>
<p>到这里整个新主节点的选择就完成了。</p>
<h3>小结</h3>
<p>本文从动态新增的主节点通过 reshard 命令重新分配槽位开始，讲了槽位定位的算法以及负载均衡的实现方法，还使用代码的方式演示了如何在程序中操作 Redis 集群，最后讲了 Redis 集群故障发现以及故障转移、新主节点选举的整个流程，希望对你理解 Redis 的集群有帮助。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="39&#32;实战：Redis&#32;集群模式（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="41&#32;案例：Redis&#32;问题汇总和相关解决方案.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a974bf370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Redis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
