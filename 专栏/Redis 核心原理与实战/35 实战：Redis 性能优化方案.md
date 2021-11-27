<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>35 实战：Redis 性能优化方案.md</title>
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

                    <a class="current-tab" href="35&#32;实战：Redis&#32;性能优化方案.md">35 实战：Redis 性能优化方案.md</a>
                    

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

                    
                    <a href="40&#32;实战：Redis&#32;集群模式（下）.md">40 实战：Redis 集群模式（下）.md</a>

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
                        <div><h1>35 实战：Redis 性能优化方案</h1>
<p>Redis 是基于单线程模型实现的，也就是 Redis 是使用一个线程来处理所有的客户端请求的，尽管 Redis 使用了非阻塞式 IO，并且对各种命令都做了优化（大部分命令操作时间复杂度都是 O(1)），但由于 Redis 是单线程执行的特点，因此它对性能的要求更加苛刻，本文我们将通过一些优化手段，让 Redis 更加高效的运行。</p>
<p>本文我们将使用以下手段，来提升 Redis 的运行速度：</p>
<ol>
<li>缩短键值对的存储长度；</li>
<li>使用 lazy free（延迟删除）特性；</li>
<li>设置键值的过期时间；</li>
<li>禁用耗时长的查询命令；</li>
<li>使用 slowlog 优化耗时命令；</li>
<li>使用 Pipeline 批量操作数据；</li>
<li>避免大量数据同时失效；</li>
<li>客户端使用优化；</li>
<li>限制 Redis 内存大小；</li>
<li>使用物理机而非虚拟机安装 Redis 服务；</li>
<li>检查数据持久化策略；</li>
<li>使用分布式架构来增加读写速度。</li>
</ol>
<h3>缩短键值对的存储长度</h3>
<p>键值对的长度是和性能成反比的，比如我们来做一组写入数据的性能测试，执行结果如下：</p>
<table>
<thead>
<tr>
<th align="left">数据量</th>
<th align="left">key 大小</th>
<th align="left">value 大小</th>
<th align="left">string:set 平均耗时</th>
<th align="left">hash:hset 平均耗时</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">100w</td>
<td align="left">20byte</td>
<td align="left">512byte</td>
<td align="left">1.13 微秒</td>
<td align="left">10.28 微秒</td>
</tr>
<tr>
<td align="left">100w</td>
<td align="left">20byte</td>
<td align="left">200byte</td>
<td align="left">0.74 微秒</td>
<td align="left">8.08 微秒</td>
</tr>
<tr>
<td align="left">100w</td>
<td align="left">20byte</td>
<td align="left">100byte</td>
<td align="left">0.65 微秒</td>
<td align="left">7.92 微秒</td>
</tr>
<tr>
<td align="left">100w</td>
<td align="left">20byte</td>
<td align="left">50byte</td>
<td align="left">0.59 微秒</td>
<td align="left">6.74 微秒</td>
</tr>
<tr>
<td align="left">100w</td>
<td align="left">20byte</td>
<td align="left">20byte</td>
<td align="left">0.55 微秒</td>
<td align="left">6.60 微秒</td>
</tr>
<tr>
<td align="left">100w</td>
<td align="left">20byte</td>
<td align="left">5byte</td>
<td align="left">0.53 微秒</td>
<td align="left">6.53 微秒</td>
</tr>
</tbody>
</table>
<p>从以上数据可以看出，在 key 不变的情况下，value 值越大操作效率越慢，因为 Redis 对于同一种数据类型会使用不同的内部编码进行存储，比如字符串的内部编码就有三种：int（整数编码）、raw（优化内存分配的字符串编码）、embstr（动态字符串编码），这是因为 Redis 的作者是想通过不同编码实现效率和空间的平衡，然而数据量越大使用的内部编码就越复杂，而越是复杂的内部编码存储的性能就越低。</p>
<p>这还只是写入时的速度，当键值对内容较大时，还会带来另外几个问题：</p>
<ul>
<li>内容越大需要的持久化时间就越长，需要挂起的时间越长，Redis 的性能就会越低；</li>
<li>内容越大在网络上传输的内容就越多，需要的时间就越长，整体的运行速度就越低；</li>
<li>内容越大占用的内存就越多，就会更频繁地触发内存淘汰机制，从而给 Redis 带来了更多的运行负担。</li>
</ul>
<p>因此在保证完整语义的同时，我们要尽量地缩短键值对的存储长度，必要时要对数据进行序列化和压缩再存储，以 Java 为例，序列化我们可以使用 protostuff 或 kryo，压缩我们可以使用 snappy。</p>
<h3>使用 lazy free 特性</h3>
<p>lazy free 特性是 Redis 4.0 新增的一个非常实用的功能，它可以理解为惰性删除或延迟删除。意思是在删除的时候提供异步延时释放键值的功能，把键值释放操作放在 BIO（Background I/O）单独的子线程处理中，以减少删除对 Redis 主线程的阻塞，可以有效地避免删除 big key 时带来的性能和可用性问题。</p>
<p>lazy free 对应了 4 种场景，默认都是关闭的：</p>
<pre><code class="language-xml">lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
slave-lazy-flush no

</code></pre>
<p>它们代表的含义如下：</p>
<ul>
<li>lazyfree-lazy-eviction：表示当 Redis 运行内存超过 maxmeory 时，是否开启 lazy free 机制删除；</li>
<li>lazyfree-lazy-expire：表示设置了过期时间的键值，当过期之后是否开启 lazy free 机制删除；</li>
<li>lazyfree-lazy-server-del：有些指令在处理已存在的键时，会带有一个隐式的 del 键的操作，比如 rename 命令，当目标键已存在，Redis 会先删除目标键，如果这些目标键是一个 big key，就会造成阻塞删除的问题，此配置表示在这种场景中是否开启 lazy free 机制删除；</li>
<li>slave-lazy-flush：针对 slave（从节点）进行全量数据同步，slave 在加载 master 的 RDB 文件前，会运行 flushall 来清理自己的数据，它表示此时是否开启 lazy free 机制删除。</li>
</ul>
<p>建议开启其中的 lazyfree-lazy-eviction、lazyfree-lazy-expire、lazyfree-lazy-server-del 等配置，这样就可以有效的提高主线程的执行效率。</p>
<h3>设置键值的过期时间</h3>
<p>我们应该根据实际的业务情况，对键值设置合理的过期时间，这样 Redis 会帮你自动清除过期的键值对，以节约对内存的占用，以避免键值过多的堆积，频繁的触发内存淘汰策略。</p>
<h3>禁用耗时长的查询命令</h3>
<p>Redis 绝大多数读写命令的时间复杂度都在 O(1) 到 O(N) 之间，在官方文档对每命令都有时间复杂度说明，地址：</p>
<blockquote>
<p><a href="https://redis.io/commands">https://redis.io/commands</a></p>
</blockquote>
<p>如下图所示：</p>
<p><img src="assets/74791f10-8008-11ea-8e01-8df59dc64941" alt="img" /></p>
<p>其中 O(1) 表示可以安全使用的，而 O(N) 就应该当心了，N 表示不确定，数据越大查询的速度可能会越慢。因为 Redis 只用一个线程来做数据查询，如果这些指令耗时很长，就会阻塞 Redis，造成大量延时。</p>
<p>要避免 O(N) 命令对 Redis 造成的影响，可以从以下几个方面入手改造：</p>
<ul>
<li>决定禁止使用 keys 命令；</li>
<li>避免一次查询所有的成员，要使用 scan 命令进行分批的，游标式的遍历；</li>
<li>通过机制严格控制 Hash、Set、Sorted Set 等结构的数据大小；</li>
<li>将排序、并集、交集等操作放在客户端执行，以减少 Redis 服务器运行压力；</li>
<li>删除（del）一个大数据的时候，可能会需要很长时间，所以建议用异步删除的方式 unlink，它会启动一个新的线程来删除目标数据，而不阻塞 Redis 的主线程。</li>
</ul>
<h3>使用 slowlog 优化耗时命令</h3>
<p>我们可以使用 slowlog 功能找出最耗时的 Redis 命令进行相关的优化，以提升 Redis 的运行速度，慢查询有两个重要的配置项：</p>
<ul>
<li>slowlog-log-slower-than：用于设置慢查询的评定时间，也就是说超过此配置项的命令，将会被当成慢操作记录在慢查询日志中，它执行单位是微秒（1 秒等于 1000000 微秒）；</li>
<li>slowlog-max-len：用来配置慢查询日志的最大记录数。</li>
</ul>
<p>我们可以根据实际的业务情况进行相应的配置，其中慢日志是按照插入的顺序倒序存入慢查询日志中，我们可以使用 <code>slowlog get n</code> 来获取相关的慢查询日志，再找到这些慢查询对应的业务进行相关的优化。</p>
<h3>使用 Pipeline 批量操作数据</h3>
<p>Pipeline（管道技术）是客户端提供的一种批处理技术，用于一次处理多个 Redis 命令，从而提高整个交互的性能。</p>
<p>我们使用 Java 代码来测试一下 Pipeline 和普通操作的性能对比，Pipeline 的测试代码如下：</p>
<pre><code class="language-java">public class PipelineExample {
    public static void main(String[] args) {
        Jedis jedis = new Jedis(&quot;127.0.0.1&quot;, 6379);
        // 记录执行开始时间
        long beginTime = System.currentTimeMillis();
        // 获取 Pipeline 对象
        Pipeline pipe = jedis.pipelined();
        // 设置多个 Redis 命令
        for (int i = 0; i &lt; 100; i++) {
            pipe.set(&quot;key&quot; + i, &quot;val&quot; + i);
            pipe.del(&quot;key&quot;+i);
        }
        // 执行命令
        pipe.sync();
        // 记录执行结束时间
        long endTime = System.currentTimeMillis();
        System.out.println(&quot;执行耗时：&quot; + (endTime - beginTime) + &quot;毫秒&quot;);
    }
}

</code></pre>
<p>以上程序执行结果为：</p>
<pre><code>执行耗时：297毫秒

</code></pre>
<p>普通的操作代码如下：</p>
<pre><code class="language-java">public class PipelineExample {
    public static void main(String[] args) {
        Jedis jedis = new Jedis(&quot;127.0.0.1&quot;, 6379);
        // 记录执行开始时间
        long beginTime = System.currentTimeMillis();
        for (int i = 0; i &lt; 100; i++) {
            jedis.set(&quot;key&quot; + i, &quot;val&quot; + i);
            jedis.del(&quot;key&quot;+i);
        }
        // 记录执行结束时间
        long endTime = System.currentTimeMillis();
        System.out.println(&quot;执行耗时：&quot; + (endTime - beginTime) + &quot;毫秒&quot;);
    }
}

</code></pre>
<p>以上程序执行结果为：</p>
<pre><code>执行耗时：17276毫秒

</code></pre>
<p>从以上的结果可以看出，管道的执行时间是 297 毫秒，而普通命令执行时间是 17276 毫秒，管道技术要比普通的执行大约快了 58 倍。</p>
<h3>避免大量数据同时失效</h3>
<p>Redis 过期键值删除使用的是贪心策略，它每秒会进行 10 次过期扫描，此配置可在 redis.conf 进行配置，默认值是 <code>hz 10</code>，Redis 会随机抽取 20 个值，删除这 20 个键中过期的键，如果过期 key 的比例超过 25%，重复执行此流程，如下图所示：</p>
<p><img src="assets/83b48140-8008-11ea-8d11-79219621097f" alt="img" /></p>
<p>如果在大型系统中有大量缓存在同一时间同时过期，那么会导致 Redis 循环多次持续扫描删除过期字典，直到过期字典中过期键值被删除的比较稀疏为止，而在整个执行过程会导致 Redis 的读写出现明显的卡顿，卡顿的另一种原因是内存管理器需要频繁回收内存页，因此也会消耗一定的 CPU。</p>
<p>为了避免这种卡顿现象的产生，我们需要预防大量的缓存在同一时刻一起过期，最简单的解决方案就是在过期时间的基础上添加一个指定范围的随机数。</p>
<h3>客户端使用优化</h3>
<p>在客户端的使用上我们除了要尽量使用 Pipeline 的技术外，还需要注意要尽量使用 Redis 连接池，而不是频繁创建销毁 Redis 连接，这样就可以减少网络传输次数和减少了非必要调用指令。</p>
<h3>限制 Redis 内存大小</h3>
<p>在 64 位操作系统中 Redis 的内存大小是没有限制的，也就是配置项 <code>maxmemory &lt;bytes&gt;</code> 是被注释掉的，这样就会导致在物理内存不足时，使用 swap 空间既交换空间，而当操心系统将 Redis 所用的内存分页移至 swap 空间时，将会阻塞 Redis 进程，导致 Redis 出现延迟，从而影响 Redis 的整体性能。因此我们需要限制 Redis 的内存大小为一个固定的值，当 Redis 的运行到达此值时会触发内存淘汰策略，<strong>内存淘汰策略在 Redis 4.0 之后有 8 种</strong>：</p>
<ul>
<li><strong>noeviction</strong>：不淘汰任何数据，当内存不足时，新增操作会报错，Redis 默认内存淘汰策略；</li>
<li><strong>allkeys-lru</strong>：淘汰整个键值中最久未使用的键值；</li>
<li><strong>allkeys-random</strong>：随机淘汰任意键值;</li>
<li><strong>volatile-lru</strong>：淘汰所有设置了过期时间的键值中最久未使用的键值；</li>
<li><strong>volatile-random</strong>：随机淘汰设置了过期时间的任意键值；</li>
<li><strong>volatile-ttl</strong>：优先淘汰更早过期的键值。</li>
</ul>
<p>在 Redis 4.0 版本中又新增了 2 种淘汰策略：</p>
<ul>
<li><strong>volatile-lfu</strong>：淘汰所有设置了过期时间的键值中，最少使用的键值；</li>
<li><strong>allkeys-lfu</strong>：淘汰整个键值中最少使用的键值。</li>
</ul>
<p>其中 allkeys-xxx 表示从所有的键值中淘汰数据，而 volatile-xxx 表示从设置了过期键的键值中淘汰数据。</p>
<p>我们可以根据实际的业务情况进行设置，默认的淘汰策略不淘汰任何数据，在新增时会报错。</p>
<h3>使用物理机而非虚拟机</h3>
<p>在虚拟机中运行 Redis 服务器，因为和物理机共享一个物理网口，并且一台物理机可能有多个虚拟机在运行，因此在内存占用上和网络延迟方面都会有很糟糕的表现，我们可以通过 <code>./redis-cli --intrinsic-latency 100</code> 命令查看延迟时间，如果对 Redis 的性能有较高要求的话，应尽可能在物理机上直接部署 Redis 服务器。</p>
<h3>检查数据持久化策略</h3>
<p>Redis 的持久化策略是将内存数据复制到硬盘上，这样才可以进行容灾恢复或者数据迁移，但维护此持久化的功能，需要很大的性能开销。</p>
<p>在 Redis 4.0 之后，Redis 有 3 种持久化的方式：</p>
<ul>
<li>RDB（Redis DataBase，快照方式）将某一个时刻的内存数据，以二进制的方式写入磁盘；</li>
<li>AOF（Append Only File，文件追加方式），记录所有的操作命令，并以文本的形式追加到文件中；</li>
<li>混合持久化方式，Redis 4.0 之后新增的方式，混合持久化是结合了 RDB 和 AOF 的优点，在写入的时候，先把当前的数据以 RDB 的形式写入文件的开头，再将后续的操作命令以 AOF 的格式存入文件，这样既能保证 Redis 重启时的速度，又能减低数据丢失的风险。</li>
</ul>
<p>RDB 和 AOF 持久化各有利弊，RDB 可能会导致一定时间内的数据丢失，而 AOF 由于文件较大则会影响 Redis 的启动速度，为了能同时拥有 RDB 和 AOF 的优点，Redis 4.0 之后新增了混合持久化的方式，因此我们在必须要进行持久化操作时，应该选择混合持久化的方式。</p>
<p>查询是否开启混合持久化可以使用 <code>config get aof-use-rdb-preamble</code> 命令，执行结果如下图所示：</p>
<p><img src="assets/b9166dd0-8008-11ea-8d11-79219621097f" alt="img" /></p>
<p>其中 yes 表示已经开启混合持久化，no 表示关闭，Redis 5.0 默认值为 yes。</p>
<p>如果是其他版本的 Redis 首先需要检查一下，是否已经开启了混合持久化，如果关闭的情况下，可以通过以下两种方式开启：</p>
<ul>
<li>通过命令行开启</li>
<li>通过修改 Redis 配置文件开启</li>
</ul>
<h4><strong>通过命令行开启</strong></h4>
<p>使用命令 <code>config set aof-use-rdb-preamble yes</code> 执行结果如下图所示：</p>
<p><img src="assets/d91028b0-8008-11ea-b6fa-0f8087ec57b4" alt="img" /></p>
<p>命令行设置配置的缺点是重启 Redis 服务之后，设置的配置就会失效。</p>
<h4><strong>通过修改 Redis 配置文件开启</strong></h4>
<p>在 Redis 的根路径下找到 redis.conf 文件，把配置文件中的 <code>aof-use-rdb-preamble no</code> 改为 <code>aof-use-rdb-preamble yes</code> 如下图所示：</p>
<p><img src="assets/efdb93e0-8008-11ea-892e-3d2bc7939884" alt="img" /></p>
<p>配置完成之后，需要重启 Redis 服务器，配置才能生效，但修改配置文件的方式，在每次重启 Redis 服务之后，配置信息不会丢失。</p>
<p>需要注意的是，在非必须进行持久化的业务中，可以关闭持久化，这样可以有效地提升 Redis 的运行速度，不会出现间歇性卡顿的困扰。</p>
<h3>使用分布式架构来增加读写速度</h3>
<p>Redis 分布式架构有三个重要的手段：</p>
<ul>
<li>主从同步</li>
<li>哨兵模式</li>
<li>Redis Cluster 集群</li>
</ul>
<p>使用主从同步功能我们可以把写入放到主库上执行，把读功能转移到从服务上，因此就可以在单位时间内处理更多的请求，从而提升的 Redis 整体的运行速度。</p>
<p>而哨兵模式是对于主从功能的升级，但当主节点奔溃之后，无需人工干预就能自动恢复 Redis 的正常使用。</p>
<p>Redis Cluster 是 Redis 3.0 正式推出的，Redis 集群是通过将数据分散存储到多个节点上，来平衡各个节点的负载压力。</p>
<p>Redis Cluster 采用虚拟哈希槽分区，所有的键根据哈希函数映射到 0~16383 整数槽内，计算公式：</p>
<pre><code>slot = CRC16(key) &amp; 16383

</code></pre>
<p>每一个节点负责维护一部分槽以及槽所映射的键值数据。这样 Redis 就可以把读写压力从一台服务器，分散给多台服务器了，因此性能会有很大的提升。</p>
<p>在这三个功能中，我们只需要使用一个就行了，毫无疑问 Redis Cluster 应该是首选的实现方案，它可以把读写压力自动地分担给更多的服务器，并且拥有自动容灾的能力。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="34&#32;实战：Redis&#32;慢查询.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="36&#32;实战：Redis&#32;主从同步.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a72983770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
