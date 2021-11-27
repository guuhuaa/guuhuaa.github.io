<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>33 实战：Redis 性能测试.md</title>
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

                    <a class="current-tab" href="33&#32;实战：Redis&#32;性能测试.md">33 实战：Redis 性能测试.md</a>
                    

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
                        <div><h1>33 实战：Redis 性能测试</h1>
<h3>为什么需要性能测试？</h3>
<p>性能测试的使用场景有很多，例如以下几个：</p>
<ol>
<li>技术选型，比如测试 Memcached 和 Redis；</li>
<li>对比单机 Redis 和集群 Redis 的吞吐量；</li>
<li>评估不同类型的存储性能，例如集合和有序集合；</li>
<li>对比开启持久化和关闭持久化的吞吐量；</li>
<li>对比调优和未调优的吞吐量；</li>
<li>对比不同 Redis 版本的吞吐量，作为是否升级的一个参考标准。</li>
</ol>
<p>等等，诸如此类的情况，我们都需要进行性能测试。</p>
<h3>性能测试的几种方式</h3>
<p>既然性能测试使用场景那么多，那要怎么进行性能测试呢？</p>
<p>目前比较主流的性能测试分为两种：</p>
<ol>
<li>编写代码模拟并发进行性能测试；</li>
<li>使用 redis-benchmark 进行测试。</li>
</ol>
<p>因为自己编写代码进行性能测试的方式不够灵活，且很难短时间内模拟大量的并发数，所有作者并不建议使用这种方式。幸运的是 Redis 本身给我们提供了性能测试工具 redis-benchmark（Redis 基准测试），因此我们本文重点来介绍 redis-benchmark 的使用。</p>
<h3>基准测试实战</h3>
<p>redis-benchmark 位于 Redis 的 src 目录下，我们可以使用 <code>./redis-benchmark -h</code> 来查看基准测试的使用，执行结果如下：</p>
<pre><code class="language-shell">Usage: redis-benchmark [-h &lt;host&gt;] [-p &lt;port&gt;] [-c &lt;clients&gt;] [-n &lt;requests&gt;] [-k &lt;boolean&gt;]

 -h &lt;hostname&gt;      Server hostname (default 127.0.0.1)
 -p &lt;port&gt;          Server port (default 6379)
 -s &lt;socket&gt;        Server socket (overrides host and port)
 -a &lt;password&gt;      Password for Redis Auth
 -c &lt;clients&gt;       Number of parallel connections (default 50)
 -n &lt;requests&gt;      Total number of requests (default 100000)
 -d &lt;size&gt;          Data size of SET/GET value in bytes (default 3)
 --dbnum &lt;db&gt;       SELECT the specified db number (default 0)
 -k &lt;boolean&gt;       1=keep alive 0=reconnect (default 1)
 -r &lt;keyspacelen&gt;   Use random keys for SET/GET/INCR, random values for SADD
  Using this option the benchmark will expand the string __rand_int__
  inside an argument with a 12 digits number in the specified range
  from 0 to keyspacelen-1. The substitution changes every time a command
  is executed. Default tests use this to hit random keys in the
  specified range.
 -P &lt;numreq&gt;        Pipeline &lt;numreq&gt; requests. Default 1 (no pipeline).
 -e                 If server replies with errors, show them on stdout.
                    (no more than 1 error per second is displayed)
 -q                 Quiet. Just show query/sec values
 --csv              Output in CSV format
 -l                 Loop. Run the tests forever
 -t &lt;tests&gt;         Only run the comma separated list of tests. The test
                    names are the same as the ones produced as output.
 -I                 Idle mode. Just open N idle connections and wait.

</code></pre>
<p>可以看出 redis-benchmark 支持以下选项：</p>
<ul>
<li><code>-h &lt;hostname&gt;</code>：服务器的主机名（默认值为 127.0.0.1）。</li>
<li><code>-p &lt;port&gt;</code>：服务器的端口号（默认值为 6379）。</li>
<li><code>-s &lt;socket&gt;</code>：服务器的套接字（会覆盖主机名和端口号）。</li>
<li><code>-a &lt;password&gt;</code>：登录 Redis 时进行身份验证的密码。</li>
<li><code>-c &lt;clients&gt;</code>：并发的连接数量（默认值为 50）。</li>
<li><code>-n &lt;requests&gt;</code>：发出的请求总数（默认值为 100000）。</li>
<li><code>-d &lt;size&gt;</code>：SET/GET 命令所操作的值的数据大小，以字节为单位（默认值为 2）。</li>
<li><code>–dbnum &lt;db&gt;</code>：选择用于性能测试的数据库的编号（默认值为 0）。</li>
<li><code>-k &lt;boolean&gt;</code>：1 = 保持连接；0 = 重新连接（默认值为 1）。</li>
<li><code>-r &lt;keyspacelen&gt;</code>：SET/GET/INCR 命令使用随机键，SADD 命令使用随机值。通过这个选项，基准测试会将参数中的 <code>__rand_int__</code> 字符串替换为一个 12 位的整数，这个整数的取值范围从 0 到 keyspacelen-1。每次执行一条命令的时候，用于替换的整数值都会改变。通过这个参数，默认的测试方案会在指定范围之内尝试命中随机键。</li>
<li><code>-P &lt;numreq&gt;</code>：使用管道机制处理 <code>&lt;numreq&gt;</code> 条 Redis 请求。默认值为 1（不使用管道机制）。</li>
<li><code>-q</code>：静默测试，只显示 QPS 的值。</li>
<li><code>–csv</code>：将测试结果输出为 CSV 格式的文件。</li>
<li><code>-l</code>：循环测试。基准测试会永远运行下去。</li>
<li><code>-t &lt;tests&gt;</code>：基准测试只会运行列表中用逗号分隔的命令。测试命令的名称和结果输出产生的名称相同。</li>
<li><code>-I</code>：空闲模式，只会打开 N 个空闲的连接，然后等待。</li>
</ul>
<p>可以看出 redis-benchmark 带的功能还是比较全的。</p>
<h4><strong>基本使用</strong></h4>
<p>在安装 Redis 服务端的机器上，我们可以不带任何参数直接执行 <code>./redis-benchmark</code> 执行结果如下：</p>
<pre><code class="language-shell">[@iZ2ze0nc5n41zomzyqtksmZ:src]$ ./redis-benchmark
====== PING_INLINE ======
  100000 requests completed in 1.26 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.81% &lt;= 1 milliseconds
100.00% &lt;= 2 milliseconds
79302.14 requests per second

====== PING_BULK ======
  100000 requests completed in 1.29 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.83% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
77459.34 requests per second

====== SET ======
  100000 requests completed in 1.26 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.80% &lt;= 1 milliseconds
99.99% &lt;= 2 milliseconds
100.00% &lt;= 2 milliseconds
79239.30 requests per second

====== GET ======
  100000 requests completed in 1.19 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.72% &lt;= 1 milliseconds
99.95% &lt;= 15 milliseconds
100.00% &lt;= 16 milliseconds
100.00% &lt;= 16 milliseconds
84104.29 requests per second

====== INCR ======
  100000 requests completed in 1.17 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.86% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
85397.09 requests per second

====== LPUSH ======
  100000 requests completed in 1.22 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.79% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
82169.27 requests per second

====== RPUSH ======
  100000 requests completed in 1.22 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.71% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
81900.09 requests per second

====== LPOP ======
  100000 requests completed in 1.29 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.78% &lt;= 1 milliseconds
99.95% &lt;= 13 milliseconds
99.97% &lt;= 14 milliseconds
100.00% &lt;= 14 milliseconds
77399.38 requests per second

====== RPOP ======
  100000 requests completed in 1.25 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.82% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
80192.46 requests per second

====== SADD ======
  100000 requests completed in 1.25 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.74% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
80192.46 requests per second

====== HSET ======
  100000 requests completed in 1.21 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.86% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
82440.23 requests per second

====== SPOP ======
  100000 requests completed in 1.22 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.92% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
81699.35 requests per second

====== LPUSH (needed to benchmark LRANGE) ======
  100000 requests completed in 1.26 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.69% &lt;= 1 milliseconds
99.95% &lt;= 13 milliseconds
99.99% &lt;= 14 milliseconds
100.00% &lt;= 14 milliseconds
79176.56 requests per second

====== LRANGE_100 (first 100 elements) ======
  100000 requests completed in 1.25 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.57% &lt;= 1 milliseconds
99.98% &lt;= 2 milliseconds
100.00% &lt;= 2 milliseconds
80128.20 requests per second

====== LRANGE_300 (first 300 elements) ======
  100000 requests completed in 1.25 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.91% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
80064.05 requests per second

====== LRANGE_500 (first 450 elements) ======
  100000 requests completed in 1.30 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.78% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
76863.95 requests per second

====== LRANGE_600 (first 600 elements) ======
  100000 requests completed in 1.20 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.85% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
83263.95 requests per second

====== MSET (10 keys) ======
  100000 requests completed in 1.27 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.65% &lt;= 1 milliseconds
100.00% &lt;= 1 milliseconds
78740.16 requests per second

</code></pre>
<p>可以看出以上都是对常用的方法 Set、Get、Incr 等进行测试，基本能达到每秒 8W 的处理级别。</p>
<h4><strong>精简测试</strong></h4>
<p>我们可以使用 <code>./redis-benchmark -t set,get,incr -n 1000000 -q</code> 命令，来对 Redis 服务器进行精简测试，测试结果如下：</p>
<pre><code class="language-shell">[@iZ2ze0nc5n41zomzyqtksmZ:src]$ ./redis-benchmark -t set,get,incr -n 1000000 -q
SET: 81726.05 requests per second
GET: 81466.40 requests per second
INCR: 82481.03 requests per second

</code></pre>
<p>可以看出以上测试展示的结果非常的精简，这是因为我们设置了 <code>-q</code> 参数，此选项的意思是设置输出结果为精简模式，其中 <code>-t</code> 表示指定测试指令，<code>-n</code> 设置每个指令测试 100w 次。</p>
<h4><strong>管道测试</strong></h4>
<p>本课程的前面章节介绍了 Pipeline（管道）的知识，它是用于客户端把命令批量发给服务器端执行的，以此来提高程序的整体执行效率，那接下来我们测试一下 Pipeline 的吞吐量能到达多少，执行命令如下：</p>
<pre><code class="language-shell">[@iZ2ze0nc5n41zomzyqtksmZ:src]$ ./redis-benchmark -t set,get,incr -n 1000000 -q -P 10
SET: 628535.50 requests per second
GET: 654450.25 requests per second
INCR: 647249.19 requests per second

</code></pre>
<p>我们发现 Pipeline 的测试很快就执行完了，同样是每个指令执行 100w 次，可以看出 Pipeline 的性能几乎是普通命令的 8 倍， <code>-P 10</code> 表示每次执行 10 个 Redis 命令。</p>
<h3>基准测试的影响元素</h3>
<p>为什么每次执行 10 个 Redis 命令，Pipeline 的效率为什么达不到普通命令的 10 倍呢？</p>
<p>这是因为基准测试会受到很大外部因素的影响，例如以下几个：</p>
<ol>
<li>网络带宽和网络延迟可能是 Redis 操作最大的性能瓶颈，比如有 10w q/s，平均每个请求负责传输 8 KB 的字符，那我们需要的理论带宽是 7.6 Gbits/s，如果服务器配置的是 1 Gbits/s，那么一定会有很多信息在排队等候传输，因此运行效率可想而知，这也是很多 Redis 生产坏境之所以效率不高的原因；</li>
<li>CPU 可能是 Redis 运行的另一个重要的影响因素，如果 CPU 的计算能力跟不上 Redis 要求的话，也会影响 Redis 的运行效率；</li>
<li>如果 Redis 运行在虚拟设备上，性能也会受影响，因为普通操作在虚拟设备上会有额外的消耗；</li>
<li>普通操作和批量操作（Pipeline）对 Redis 的吞吐量也有很大的影响。</li>
</ol>
<h3>小结</h3>
<p>本文介绍了 Redis 自带的性能测试工具 redis-benchmark 也是 Redis 主流的性能测试工具，我们可以轻松模拟指定并发量和指定命令的测试条件，也可以模拟管道测试。测试的结果对于我们做技术选型、版本选择以及数据类型的选择上都有一定的指导意义，但需要注意 Redis 的吞吐量还受到其他因素的影响，例如带宽、CPU 等因素。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="32&#32;实战：RediSearch&#32;高性能的全文搜索引擎.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="34&#32;实战：Redis&#32;慢查询.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a684f2e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
