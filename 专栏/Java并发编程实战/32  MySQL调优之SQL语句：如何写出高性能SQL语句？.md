<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>32  MySQL调优之SQL语句：如何写出高性能SQL语句？.md</title>
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

                    
                    <a href="00&#32;开篇词你为什么需要学习并发编程？.md">00 开篇词你为什么需要学习并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;如何制定性能调优标准？.md">01  如何制定性能调优标准？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;如何制定性能调优策略？.md">02  如何制定性能调优策略？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;字符串性能优化不容小觑，百M内存轻松存储几十G数据.md">03  字符串性能优化不容小觑，百M内存轻松存储几十G数据.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;慎重使用正则表达式.md">04  慎重使用正则表达式.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;ArrayList还是LinkedList？使用不当性能差千倍.md">05  ArrayList还是LinkedList？使用不当性能差千倍.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Stream如何提高遍历集合效率？.md">06  Stream如何提高遍历集合效率？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入浅出HashMap的设计与优化.md">07  深入浅出HashMap的设计与优化.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md">08  网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;网络通信优化之序列化：避免使用Java序列化.md">09  网络通信优化之序列化：避免使用Java序列化.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;网络通信优化之通信协议：如何优化RPC网络通信？.md">10  网络通信优化之通信协议：如何优化RPC网络通信？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;答疑课堂：深入了解NIO的优化实现原理.md">11  答疑课堂：深入了解NIO的优化实现原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md">12  多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md">13  多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;多线程之锁优化（下）：使用乐观锁优化并行操作.md">14  多线程之锁优化（下）：使用乐观锁优化并行操作.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;多线程调优（上）：哪些操作导致了上下文切换？.md">15  多线程调优（上）：哪些操作导致了上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;多线程调优（下）：如何优化多线程上下文切换？.md">16  多线程调优（下）：如何优化多线程上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;并发容器的使用：识别不同场景下最优容器.md">17  并发容器的使用：识别不同场景下最优容器.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何设置线程池大小？.md">18  如何设置线程池大小？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何用协程来优化多线程业务？.md">19  如何用协程来优化多线程业务？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md">20  磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深入JVM即时编译器JIT，优化Java编译.md">21  深入JVM即时编译器JIT，优化Java编译.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;如何优化垃圾回收机制？.md">22  如何优化垃圾回收机制？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;如何优化JVM内存分配？.md">23  如何优化JVM内存分配？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;内存持续上升，我该如何排查问题？.md">24  内存持续上升，我该如何排查问题？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;答疑课堂：模块四热点问题解答.md">25  答疑课堂：模块四热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;单例模式：如何创建单一对象优化系统性能？.md">26  单例模式：如何创建单一对象优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;原型模式与享元模式：提升系统性能的利器.md">27  原型模式与享元模式：提升系统性能的利器.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;如何使用设计模式优化并发编程？.md">28  如何使用设计模式优化并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;生产者消费者模式：电商库存设计优化.md">29  生产者消费者模式：电商库存设计优化.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;装饰器模式：如何优化电商系统中复杂的商品价格策略？.md">30  装饰器模式：如何优化电商系统中复杂的商品价格策略？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;答疑课堂：模块五思考题集锦.md">31  答疑课堂：模块五思考题集锦.md</a>

                </li>
                <li>

                    <a class="current-tab" href="32&#32;&#32;MySQL调优之SQL语句：如何写出高性能SQL语句？.md">32  MySQL调优之SQL语句：如何写出高性能SQL语句？.md</a>
                    

                </li>
                <li>

                    
                    <a href="33&#32;&#32;MySQL调优之事务：高并发场景下的数据库事务调优.md">33  MySQL调优之事务：高并发场景下的数据库事务调优.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;MySQL调优之索引：索引的失效与优化.md">34  MySQL调优之索引：索引的失效与优化.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;记一次线上SQL死锁事故：如何避免死锁？.md">35  记一次线上SQL死锁事故：如何避免死锁？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;什么时候需要分表分库？.md">36  什么时候需要分表分库？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;电商系统表设计优化案例分析.md">37  电商系统表设计优化案例分析.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;数据库参数设置优化，失之毫厘差之千里.md">38  数据库参数设置优化，失之毫厘差之千里.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;答疑课堂：MySQL中InnoDB的知识点串讲.md">39  答疑课堂：MySQL中InnoDB的知识点串讲.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;如何设计更优的分布式锁？.md">41  如何设计更优的分布式锁？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;电商系统的分布式事务调优.md">42  电商系统的分布式事务调优.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;如何使用缓存优化系统性能？.md">43  如何使用缓存优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;记一次双十一抢购性能瓶颈调优.md">44  记一次双十一抢购性能瓶颈调优.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;什么是数据的强、弱一致性？.md">加餐  什么是数据的强、弱一致性？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;推荐几款常用的性能测试工具.md">加餐  推荐几款常用的性能测试工具.md</a>

                </li>
                <li>

                    
                    <a href="答疑课堂：模块三热点问题解答.md">答疑课堂：模块三热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;栉风沐雨，砥砺前行！.md">结束语  栉风沐雨，砥砺前行！.md</a>

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
                        <div><h1>32  MySQL调优之SQL语句：如何写出高性能SQL语句？</h1>
<p>你好，我是刘超。</p>
<p>从今天开始，我将带你一起学习 MySQL 的性能调优。MySQL 数据库是互联网公司使用最为频繁的数据库之一，不仅仅因为它开源免费，MySQL 卓越的性能、稳定的服务以及活跃的社区都成就了它的核心竞争力。</p>
<p>我们知道，应用服务与数据库的交互主要是通过 SQL 语句来实现的。在开发初期，我们更加关注的是使用 SQL 实现业务功能，然而系统上线后，随着生产环境数据的快速增长，之前写的很多 SQL 语句就开始暴露出性能问题。</p>
<p>在这个阶段中，我们应该尽量避免一些慢 SQL 语句的实现。但话说回来，SQL 语句慢的原因千千万，除了一些常规的慢 SQL 语句可以直接规避，其它的一味去规避也不是办法，我们还要学会如何去分析、定位到其根本原因，并总结一些常用的 SQL 调优方法，以备不时之需。</p>
<p>那么今天我们就重点看看慢 SQL 语句的几种常见诱因，从这点出发，找到最佳方法，开启高性能 SQL 语句的大门。</p>
<h2>慢 SQL 语句的几种常见诱因</h2>
<h3>1. 无索引、索引失效导致慢查询</h3>
<p>如果在一张几千万数据的表中以一个没有索引的列作为查询条件，大部分情况下查询会非常耗时，这种查询毫无疑问是一个慢 SQL 查询。所以对于大数据量的查询，我们需要建立适合的索引来优化查询。</p>
<p>虽然我们很多时候建立了索引，但在一些特定的场景下，索引还有可能会失效，所以索引失效也是导致慢查询的主要原因之一。针对这点的调优，我会在第 34 讲中详解。</p>
<h3>2. 锁等待</h3>
<p>我们常用的存储引擎有 InnoDB 和 MyISAM，前者支持行锁和表锁，后者只支持表锁。</p>
<p>如果数据库操作是基于表锁实现的，试想下，如果一张订单表在更新时，需要锁住整张表，那么其它大量数据库操作（包括查询）都将处于等待状态，这将严重影响到系统的并发性能。</p>
<p>这时，InnoDB 存储引擎支持的行锁更适合高并发场景。但在使用 InnoDB 存储引擎时，我们要特别注意行锁升级为表锁的可能。在批量更新操作时，行锁就很可能会升级为表锁。</p>
<p>MySQL 认为如果对一张表使用大量行锁，会导致事务执行效率下降，从而可能造成其它事务长时间锁等待和更多的锁冲突问题发生，致使性能严重下降，所以 MySQL 会将行锁升级为表锁。还有，行锁是基于索引加的锁，如果我们在更新操作时，条件索引失效，那么行锁也会升级为表锁。</p>
<p>因此，基于表锁的数据库操作，会导致 SQL 阻塞等待，从而影响执行速度。在一些更新操作（insert\update\delete）大于或等于读操作的情况下，MySQL 不建议使用 MyISAM 存储引擎。</p>
<p>除了锁升级之外，行锁相对表锁来说，虽然粒度更细，并发能力提升了，但也带来了新的问题，那就是死锁。因此，在使用行锁时，我们要注意避免死锁。关于死锁，我还会在第 35 讲中详解。</p>
<h3>3. 不恰当的 SQL 语句</h3>
<p>使用不恰当的 SQL 语句也是慢 SQL 最常见的诱因之一。例如，习惯使用 &lt;SELECT <em>&gt;，&lt;SELECT COUNT(</em>)&gt; SQL 语句，在大数据表中使用 &lt;LIMIT M,N&gt; 分页查询，以及对非索引字段进行排序等等。</p>
<h2>优化 SQL 语句的步骤</h2>
<p>通常，我们在执行一条 SQL 语句时，要想知道这个 SQL 先后查询了哪些表，是否使用了索引，这些数据从哪里获取到，获取到数据遍历了多少行数据等等，我们可以通过 EXPLAIN 命令来查看这些执行信息。这些执行信息被统称为执行计划。</p>
<h3>1. 通过 EXPLAIN 分析 SQL 执行计划</h3>
<p>假设现在我们使用 EXPLAIN 命令查看当前 SQL 是否使用了索引，先通过 SQL EXPLAIN 导出相应的执行计划如下：</p>
<p><img src="assets/bd11fa15122956719289afea2464eff8.jpg" alt="img" /></p>
<p>下面对图示中的每一个字段进行一个说明，从中你也能收获到很多零散的知识点。</p>
<ul>
<li>id：每个执行计划都有一个 id，如果是一个联合查询，这里还将有多个 id。</li>
<li>select_type：表示 SELECT 查询类型，常见的有 SIMPLE（普通查询，即没有联合查询、子查询）、PRIMARY（主查询）、UNION（UNION 中后面的查询）、SUBQUERY（子查询）等。</li>
<li>table：当前执行计划查询的表，如果给表起别名了，则显示别名信息。</li>
<li>partitions：访问的分区表信息。</li>
<li>type：表示从表中查询到行所执行的方式，查询方式是 SQL 优化中一个很重要的指标，结果值从好到差依次是：system &gt; const &gt; eq_ref &gt; ref &gt; range &gt; index &gt; ALL。</li>
</ul>
<p><img src="assets/8fc6cb3338945524fb09a092f396fa0b.jpg" alt="img" /></p>
<ul>
<li>system/const：表中只有一行数据匹配，此时根据索引查询一次就能找到对应的数据。如果是 B + 树索引，我们知道此时索引构造成了多个层级的树，当查询的索引在树的底层时，查询效率就越低。const 表示此时索引在第一层，只需访问一层便能得到数据。</li>
</ul>
<p><img src="assets/b5ea0778ff22bdde10a57edfc353712b.jpg" alt="img" /></p>
<ul>
<li>eq_ref：使用唯一索引扫描，常见于多表连接中使用主键和唯一索引作为关联条件。</li>
</ul>
<p><img src="assets/d390d8c7bb90bdbf26775265ad451c50.jpg" alt="img" /></p>
<ul>
<li>ref：非唯一索引扫描，还可见于唯一索引最左原则匹配扫描。</li>
</ul>
<p><img src="assets/4020416795c991f68fb057b3e6b80ca4.jpg" alt="img" /></p>
<ul>
<li>range：索引范围扫描，比如，&lt;，&gt;，between 等操作。</li>
</ul>
<p><img src="assets/7f7a40f88150117f6fe0bb56f52da6c7.jpg" alt="img" /></p>
<ul>
<li>index：索引全表扫描，此时遍历整个索引树。</li>
</ul>
<p><img src="assets/d3d7221fec38845145ac0f365196427b.jpg" alt="img" /></p>
<ul>
<li>ALL：表示全表扫描，需要遍历全表来找到对应的行。</li>
<li>possible_keys：可能使用到的索引。</li>
<li>key：实际使用到的索引。</li>
<li>key_len：当前使用的索引的长度。</li>
<li>ref：关联 id 等信息。</li>
<li>rows：查找到记录所扫描的行数。</li>
<li>filtered：查找到所需记录占总扫描记录数的比例。</li>
<li>Extra：额外的信息。</li>
</ul>
<h3>2. 通过 Show Profile 分析 SQL 执行性能</h3>
<p>上述通过 EXPLAIN 分析执行计划，仅仅是停留在分析 SQL 的外部的执行情况，如果我们想要深入到 MySQL 内核中，从执行线程的状态和时间来分析的话，这个时候我们就可以选择 Profile。</p>
<p>Profile 除了可以分析执行线程的状态和时间，还支持进一步选择 ALL、CPU、MEMORY、BLOCK IO、CONTEXT SWITCHES 等类型来查询 SQL 语句在不同系统资源上所消耗的时间。以下是相关命令的注释：</p>
<pre><code>SHOW PROFILE [type [, type] ... ]
[FOR QUERY n]
[LIMIT row_count [OFFSET offset]]
 
type 参数：
| ALL：显示所有开销信息
| BLOCK IO：阻塞的输入输出次数
| CONTEXT SWITCHES：上下文切换相关开销信息
| CPU：显示 CPU 的相关开销信息 
| IPC：接收和发送消息的相关开销信息
| MEMORY ：显示内存相关的开销，目前无用
| PAGE FAULTS ：显示页面错误相关开销信息
| SOURCE ：列出相应操作对应的函数名及其在源码中的调用位置 (行数) 
| SWAPS：显示 swap 交换次数的相关开销信息
</code></pre>
<p>值得注意的是，MySQL 是在 5.0.37 版本之后才支持 Show Profile 功能的，如果你不太确定的话，可以通过 select @@have_profiling 查询是否支持该功能，如下图所示：</p>
<p><img src="assets/76a42789a838dfd6b1735c41dd9f8c45.jpg" alt="img" /></p>
<p>最新的 MySQL 版本是默认开启 Show Profile 功能的，但在之前的旧版本中是默认关闭该功能的，你可以通过 set 语句在 Session 级别开启该功能：</p>
<p><img src="assets/840fbe1ecdf7526fdc818f4639e22091.jpg" alt="img" /></p>
<p>Show Profiles 只显示最近发给服务器的 SQL 语句，默认情况下是记录最近已执行的 15 条记录，我们可以重新设置 profiling_history_size 增大该存储记录，最大值为 100。</p>
<p><img src="assets/5488fde01df647508d60b9a77cd1f14f.jpg" alt="img" /></p>
<p>获取到 Query_ID 之后，我们再通过 Show Profile for Query ID 语句，就能够查看到对应 Query_ID 的 SQL 语句在执行过程中线程的每个状态所消耗的时间了：</p>
<p><img src="assets/dc7e4046ddd22438c21690e5bc38c123.jpg" alt="img" /></p>
<p>通过以上分析可知：SELECT COUNT(*) FROM <code>order</code>; SQL 语句在 Sending data 状态所消耗的时间最长，这是因为在该状态下，MySQL 线程开始读取数据并返回到客户端，此时有大量磁盘 I/O 操作。</p>
<h2>常用的 SQL 优化</h2>
<p>在使用一些常规的 SQL 时，如果我们通过一些方法和技巧来优化这些 SQL 的实现，在性能上就会比使用常规通用的实现方式更加优越，甚至可以将 SQL 语句的性能提升到另一个数量级。</p>
<h3>1. 优化分页查询</h3>
<p>通常我们是使用 &lt;LIMIT M,N&gt; + 合适的 order by 来实现分页查询，这种实现方式在没有任何索引条件支持的情况下，需要做大量的文件排序操作（file sort），性能将会非常得糟糕。如果有对应的索引，通常刚开始的分页查询效率会比较理想，但越往后，分页查询的性能就越差。</p>
<p>这是因为我们在使用 LIMIT 的时候，偏移量 M 在分页越靠后的时候，值就越大，数据库检索的数据也就越多。例如 LIMIT 10000,10 这样的查询，数据库需要查询 10010 条记录，最后返回 10 条记录。也就是说将会有 10000 条记录被查询出来没有被使用到。</p>
<p>我们模拟一张 10 万数量级的 order 表，进行以下分页查询：</p>
<pre><code>select * from `demo`.`order` order by order_no limit 10000, 20;

</code></pre>
<p>通过 EXPLAIN 分析可知：该查询使用到了索引，扫描行数为 10020 行，但所用查询时间为 0.018s，相对来说时间偏长了。</p>
<p><img src="assets/80efe0ba8feb86baa20834fd48c302fe.jpg" alt="img" /></p>
<p><img src="assets/58e2377b2adcded4c454d410bbab7d1c.jpg" alt="img" /></p>
<ul>
<li>利用子查询优化分页查询</li>
</ul>
<p>以上分页查询的问题在于，我们查询获取的 10020 行数据结果都返回给我们了，我们能否先查询出所需要的 20 行数据中的最小 ID 值，然后通过偏移量返回所需要的 20 行数据给我们呢？我们可以通过索引覆盖扫描，使用子查询的方式来实现分页查询：</p>
<pre><code>select * from `demo`.`order` where id&gt; (select id from `demo`.`order` order by order_no limit 10000, 1)  limit 20;

</code></pre>
<p>通过 EXPLAIN 分析可知：子查询遍历索引的范围跟上一个查询差不多，而主查询扫描了更多的行数，但执行时间却减少了，只有 0.004s。这就是因为返回行数只有 20 行了，执行效率得到了明显的提升。</p>
<p><img src="assets/10e46817482166d205f319cd0512942e.jpg" alt="img" /></p>
<p><img src="assets/492ddbbe2ef47d63a6dc797fd44c16bb.jpg" alt="img" /></p>
<h3>2. 优化 SELECT COUNT(*)</h3>
<p>COUNT() 是一个聚合函数，主要用来统计行数，有时候也用来统计某一列的行数量（不统计 NULL 值的行）。我们平时最常用的就是 COUNT(*) 和 COUNT(1) 这两种方式了，其实两者没有明显的区别，在拥有主键的情况下，它们都是利用主键列实现了行数的统计。</p>
<p>但 COUNT() 函数在 MyISAM 和 InnoDB 存储引擎所执行的原理是不一样的，通常在没有任何查询条件下的 COUNT(*)，MyISAM 的查询速度要明显快于 InnoDB。</p>
<p>这是因为 MyISAM 存储引擎记录的是整个表的行数，在 COUNT(*) 查询操作时无需遍历表计算，直接获取该值即可。而在 InnoDB 存储引擎中就需要扫描表来统计具体的行数。而当带上 where 条件语句之后，MyISAM 跟 InnoDB 就没有区别了，它们都需要扫描表来进行行数的统计。</p>
<p>如果对一张大表经常做 SELECT COUNT(*) 操作，这肯定是不明智的。那么我们该如何对大表的 COUNT() 进行优化呢？</p>
<ul>
<li>使用近似值</li>
</ul>
<p>有时候某些业务场景并不需要返回一个精确的 COUNT 值，此时我们可以使用近似值来代替。我们可以使用 EXPLAIN 对表进行估算，要知道，执行 EXPLAIN 并不会真正去执行查询，而是返回一个估算的近似值。</p>
<ul>
<li>增加汇总统计</li>
</ul>
<p>如果需要一个精确的 COUNT 值，我们可以额外新增一个汇总统计表或者缓存字段来统计需要的 COUNT 值，这种方式在新增和删除时有一定的成本，但却可以大大提升 COUNT() 的性能。</p>
<h3>3. 优化 SELECT *</h3>
<p>我曾经看过很多同事习惯在只查询一两个字段时，都使用 select * from table where xxx 这样的 SQL 语句，这种写法在特定的环境下会存在一定的性能损耗。</p>
<p>MySQL 常用的存储引擎有 MyISAM 和 InnoDB，其中 InnoDB 在默认创建主键时会创建主键索引，而主键索引属于聚族索引，即在存储数据时，索引是基于 B + 树构成的，具体的行数据则存储在叶子节点。</p>
<p>而 MyISAM 默认创建的主键索引、二级索引以及 InnoDB 的二级索引都属于非聚族索引，即在存储数据时，索引是基于 B + 树构成的，而叶子节点存储的是主键值。</p>
<p>假设我们的订单表是基于 InnoDB 存储引擎创建的，且存在 order_no、status 两列组成的组合索引。此时，我们需要根据订单号查询一张订单表的 status，如果我们使用 select * from order where order_no='xxx’来查询，则先会查询组合索引，通过组合索引获取到主键 ID，再通过主键 ID 去主键索引中获取对应行所有列的值。</p>
<p>如果我们使用 select order_no, status from order where order_no='xxx’来查询，则只会查询组合索引，通过组合索引获取到对应的 order_no 和 status 的值。如果你对这些索引还不够熟悉，请重点关注之后的第 34 讲，那一讲会详述数据库索引的相关内容。</p>
<h2>总结</h2>
<p>在开发中，我们要尽量写出高性能的 SQL 语句，但也无法避免一些慢 SQL 语句的出现，或因为疏漏，或因为实际生产环境与开发环境有所区别，这些都是诱因。面对这种情况，我们可以打开慢 SQL 配置项，记录下都有哪些 SQL 超过了预期的最大执行时间。首先，我们可以通过以下命令行查询是否开启了记录慢 SQL 的功能，以及最大的执行时间是多少：</p>
<pre><code>Show variables like 'slow_query%';
Show variables like 'long_query_time';
</code></pre>
<p>如果没有开启，我们可以通过以下设置来开启：</p>
<pre><code>set global slow_query_log='ON'; // 开启慢 SQL 日志
set global slow_query_log_file='/var/lib/mysql/test-slow.log';// 记录日志地址
set global long_query_time=1;// 最大执行时间
</code></pre>
<p>除此之外，很多数据库连接池中间件也有分析慢 SQL 的功能。总之，我们要在编程中避免低性能的 SQL 操作出现，除了要具备一些常用的 SQL 优化技巧之外，还要充分利用一些 SQL 工具，实现 SQL 性能分析与监控。</p>
<h2>思考题</h2>
<p>假设有一张订单表 order，主要包含了主键订单编码 order_no、订单状态 status、提交时间 create_time 等列，并且创建了 status 列索引和 create_time 列索引。此时通过创建时间降序获取状态为 1 的订单编码，以下是具体实现代码：</p>
<pre><code>select order_no from order where status =1 order by create_time desc

</code></pre>
<p>你知道其中的问题所在吗？我们又该如何优化？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="31&#32;&#32;答疑课堂：模块五思考题集锦.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="33&#32;&#32;MySQL调优之事务：高并发场景下的数据库事务调优.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43445ecb7270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Java%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
