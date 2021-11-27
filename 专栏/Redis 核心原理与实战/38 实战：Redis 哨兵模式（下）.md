<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>38 实战：Redis 哨兵模式（下）.md</title>
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

                    <a class="current-tab" href="38&#32;实战：Redis&#32;哨兵模式（下）.md">38 实战：Redis 哨兵模式（下）.md</a>
                    

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
                        <div><h1>38 实战：Redis 哨兵模式（下）</h1>
<p>上一篇我们介绍了 Redis Sentinel 的搭建和运行原理，本文我们重点来看下 Sentinel 的命令操作和代码实战。</p>
<h3>Sentinel 命令操作</h3>
<p>要使用 Sentinel 实现要连接到 Sentinel 服务器，和连接 Redis 服务相同，我们可以使用 redis-cli 来连接 Sentinel，如下命令所示：</p>
<pre><code class="language-shell">[@iZ2ze0nc5n41zomzyqtksmZ:~]$ redis-cli -h 127.0.0.1 -p 26379 -a pwd654321
127.0.0.1:26379&gt; ping
PONG

</code></pre>
<p>其中：</p>
<ul>
<li>-h 后面输入的是 Sentinel 的 IP；</li>
<li>-p 后面输入的是 Sentinel 的端口，默认是 26379；</li>
<li>-a 后面输入的是密码。</li>
</ul>
<p>Sentinel 的端口号可以在 sentinel.conf 里面配置，通过 port 选项设置。</p>
<p>注意：<strong>Sentinel 可以监视多台主节点，而不是只能监视一台服务器</strong>。想要监视多台主节点只需要在配置文件中设置多个 <code>sentinel monitor master-name ip port quorum</code> 即可，我们通过 master-name 来区分不同的主节点。</p>
<h4><strong>查询所有被监控的主服务器信息</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel masters
1)  1) &quot;name&quot;
    2) &quot;mymaster&quot;
    3) &quot;ip&quot;
    4) &quot;127.0.0.1&quot;
    5) &quot;port&quot;
    6) &quot;6377&quot;
    7) &quot;runid&quot;
    8) &quot;eb3552c6fc8974f91466c4ada90fe23ef30fd89c&quot;
    9) &quot;flags&quot;
   10) &quot;master&quot;
   11) &quot;link-pending-commands&quot;
   12) &quot;0&quot;
   13) &quot;link-refcount&quot;
   14) &quot;1&quot;
   15) &quot;last-ping-sent&quot;
   16) &quot;0&quot;
   17) &quot;last-ok-ping-reply&quot;
   18) &quot;400&quot;
   19) &quot;last-ping-reply&quot;
   20) &quot;400&quot;
   21) &quot;down-after-milliseconds&quot;
   22) &quot;30000&quot;
   23) &quot;info-refresh&quot;
   24) &quot;5731&quot;
   25) &quot;role-reported&quot;
   26) &quot;master&quot;
   27) &quot;role-reported-time&quot;
   28) &quot;75963321&quot;
   29) &quot;config-epoch&quot;
   30) &quot;7&quot;
   31) &quot;num-slaves&quot;
   32) &quot;2&quot;
   33) &quot;num-other-sentinels&quot;
   34) &quot;1&quot;
   35) &quot;quorum&quot;
   36) &quot;2&quot;
   37) &quot;failover-timeout&quot;
   38) &quot;180000&quot;
   39) &quot;parallel-syncs&quot;
   40) &quot;1&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>sentinel masters

</code></pre>
<p>因为我们配置的 Sentinel 只监视了一台主服务器，所以只有一台服务器的信息。</p>
<h4><strong>查询某个主节点的信息</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel master mymaster
 1) &quot;name&quot;
 2) &quot;mymaster&quot;
 3) &quot;ip&quot;
 4) &quot;127.0.0.1&quot;
 5) &quot;port&quot;
 6) &quot;6377&quot;
 7) &quot;runid&quot;
 8) &quot;eb3552c6fc8974f91466c4ada90fe23ef30fd89c&quot;
 9) &quot;flags&quot;
10) &quot;master&quot;
11) &quot;link-pending-commands&quot;
12) &quot;0&quot;
13) &quot;link-refcount&quot;
14) &quot;1&quot;
15) &quot;last-ping-sent&quot;
16) &quot;0&quot;
17) &quot;last-ok-ping-reply&quot;
18) &quot;250&quot;
19) &quot;last-ping-reply&quot;
20) &quot;250&quot;
21) &quot;down-after-milliseconds&quot;
22) &quot;30000&quot;
23) &quot;info-refresh&quot;
24) &quot;8191&quot;
25) &quot;role-reported&quot;
26) &quot;master&quot;
27) &quot;role-reported-time&quot;
28) &quot;76096303&quot;
29) &quot;config-epoch&quot;
30) &quot;7&quot;
31) &quot;num-slaves&quot;
32) &quot;2&quot;
33) &quot;num-other-sentinels&quot;
34) &quot;1&quot;
35) &quot;quorum&quot;
36) &quot;2&quot;
37) &quot;failover-timeout&quot;
38) &quot;180000&quot;
39) &quot;parallel-syncs&quot;
40) &quot;1&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>sentinel master master-name

</code></pre>
<h4><strong>查看某个主节点的 IP 和端口</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel get-master-addr-by-name mymaster
1) &quot;127.0.0.1&quot;
2) &quot;6377&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>sentinel get-master-addr-by-name master-name

</code></pre>
<h4><strong>查询从节点的信息</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel slaves mymaster #获取方式一
1)  1) &quot;name&quot;
    2) &quot;127.0.0.1:6379&quot;
    3) &quot;ip&quot;
    4) &quot;127.0.0.1&quot;
    5) &quot;port&quot;
    6) &quot;6379&quot;
    7) &quot;runid&quot;
    8) &quot;14734d6065d745d89f115ca4735e7eeeeaa1a59b&quot;
    9) &quot;flags&quot;
   10) &quot;slave&quot;
   11) &quot;link-pending-commands&quot;
   12) &quot;0&quot;
   13) &quot;link-refcount&quot;
   14) &quot;1&quot;
   15) &quot;last-ping-sent&quot;
   16) &quot;0&quot;
   17) &quot;last-ok-ping-reply&quot;
   18) &quot;389&quot;
   19) &quot;last-ping-reply&quot;
   20) &quot;389&quot;
   21) &quot;down-after-milliseconds&quot;
   22) &quot;30000&quot;
   23) &quot;info-refresh&quot;
   24) &quot;390&quot;
   25) &quot;role-reported&quot;
   26) &quot;slave&quot;
   27) &quot;role-reported-time&quot;
   28) &quot;982798&quot;
   29) &quot;master-link-down-time&quot;
   30) &quot;1582192784000&quot;
   31) &quot;master-link-status&quot;
   32) &quot;err&quot;
   33) &quot;master-host&quot;
   34) &quot;127.0.0.1&quot;
   35) &quot;master-port&quot;
   36) &quot;6377&quot;
   37) &quot;slave-priority&quot;
   38) &quot;100&quot;
   39) &quot;slave-repl-offset&quot;
   40) &quot;1&quot;
2)  1) &quot;name&quot;
    2) &quot;127.0.0.1:6378&quot;
    3) &quot;ip&quot;
    4) &quot;127.0.0.1&quot;
    5) &quot;port&quot;
    6) &quot;6378&quot;
    7) &quot;runid&quot;
    8) &quot;f9d69479ace6c9eb4a6dffa58ebc1ddf3de456e0&quot;
    9) &quot;flags&quot;
   10) &quot;slave&quot;
   11) &quot;link-pending-commands&quot;
   12) &quot;0&quot;
   13) &quot;link-refcount&quot;
   14) &quot;1&quot;
   15) &quot;last-ping-sent&quot;
   16) &quot;0&quot;
   17) &quot;last-ok-ping-reply&quot;
   18) &quot;390&quot;
   19) &quot;last-ping-reply&quot;
   20) &quot;390&quot;
   21) &quot;down-after-milliseconds&quot;
   22) &quot;30000&quot;
   23) &quot;info-refresh&quot;
   24) &quot;4004&quot;
   25) &quot;role-reported&quot;
   26) &quot;slave&quot;
   27) &quot;role-reported-time&quot;
   28) &quot;76212633&quot;
   29) &quot;master-link-down-time&quot;
   30) &quot;0&quot;
   31) &quot;master-link-status&quot;
   32) &quot;ok&quot;
   33) &quot;master-host&quot;
   34) &quot;127.0.0.1&quot;
   35) &quot;master-port&quot;
   36) &quot;6377&quot;
   37) &quot;slave-priority&quot;
   38) &quot;100&quot;
   39) &quot;slave-repl-offset&quot;
   40) &quot;10811245&quot;
127.0.0.1:26379&gt; sentinel replicas mymaster #获取方式二
1)  1) &quot;name&quot;
    2) &quot;127.0.0.1:6379&quot;
    3) &quot;ip&quot;
    4) &quot;127.0.0.1&quot;
    5) &quot;port&quot;
    6) &quot;6379&quot;
    7) &quot;runid&quot;
    8) &quot;14734d6065d745d89f115ca4735e7eeeeaa1a59b&quot;
    9) &quot;flags&quot;
   10) &quot;slave&quot;
   11) &quot;link-pending-commands&quot;
   12) &quot;0&quot;
   13) &quot;link-refcount&quot;
   14) &quot;1&quot;
   15) &quot;last-ping-sent&quot;
   16) &quot;0&quot;
   17) &quot;last-ok-ping-reply&quot;
   18) &quot;100&quot;
   19) &quot;last-ping-reply&quot;
   20) &quot;100&quot;
   21) &quot;down-after-milliseconds&quot;
   22) &quot;30000&quot;
   23) &quot;info-refresh&quot;
   24) &quot;100&quot;
   25) &quot;role-reported&quot;
   26) &quot;slave&quot;
   27) &quot;role-reported-time&quot;
   28) &quot;1071687&quot;
   29) &quot;master-link-down-time&quot;
   30) &quot;1582192873000&quot;
   31) &quot;master-link-status&quot;
   32) &quot;err&quot;
   33) &quot;master-host&quot;
   34) &quot;127.0.0.1&quot;
   35) &quot;master-port&quot;
   36) &quot;6377&quot;
   37) &quot;slave-priority&quot;
   38) &quot;100&quot;
   39) &quot;slave-repl-offset&quot;
   40) &quot;1&quot;
2)  1) &quot;name&quot;
    2) &quot;127.0.0.1:6378&quot;
    3) &quot;ip&quot;
    4) &quot;127.0.0.1&quot;
    5) &quot;port&quot;
    6) &quot;6378&quot;
    7) &quot;runid&quot;
    8) &quot;f9d69479ace6c9eb4a6dffa58ebc1ddf3de456e0&quot;
    9) &quot;flags&quot;
   10) &quot;slave&quot;
   11) &quot;link-pending-commands&quot;
   12) &quot;0&quot;
   13) &quot;link-refcount&quot;
   14) &quot;1&quot;
   15) &quot;last-ping-sent&quot;
   16) &quot;0&quot;
   17) &quot;last-ok-ping-reply&quot;
   18) &quot;100&quot;
   19) &quot;last-ping-reply&quot;
   20) &quot;100&quot;
   21) &quot;down-after-milliseconds&quot;
   22) &quot;30000&quot;
   23) &quot;info-refresh&quot;
   24) &quot;2496&quot;
   25) &quot;role-reported&quot;
   26) &quot;slave&quot;
   27) &quot;role-reported-time&quot;
   28) &quot;76301522&quot;
   29) &quot;master-link-down-time&quot;
   30) &quot;0&quot;
   31) &quot;master-link-status&quot;
   32) &quot;ok&quot;
   33) &quot;master-host&quot;
   34) &quot;127.0.0.1&quot;
   35) &quot;master-port&quot;
   36) &quot;6377&quot;
   37) &quot;slave-priority&quot;
   38) &quot;100&quot;
   39) &quot;slave-repl-offset&quot;
   40) &quot;10823208&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>sentinel replicas mymaster

</code></pre>
<p>或</p>
<pre><code>sentinel slaves master-name

</code></pre>
<h4><strong>查询 Sentinel 集群中的其他 Sentinel 信息</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel sentinels mymaster
1)  1) &quot;name&quot;
    2) &quot;6455f2f74614a71ce0a63398b2e48d6cd1cf0d06&quot;
    3) &quot;ip&quot;
    4) &quot;127.0.0.1&quot;
    5) &quot;port&quot;
    6) &quot;26377&quot;
    7) &quot;runid&quot;
    8) &quot;6455f2f74614a71ce0a63398b2e48d6cd1cf0d06&quot;
    9) &quot;flags&quot;
   10) &quot;sentinel&quot;
   11) &quot;link-pending-commands&quot;
   12) &quot;0&quot;
   13) &quot;link-refcount&quot;
   14) &quot;1&quot;
   15) &quot;last-ping-sent&quot;
   16) &quot;0&quot;
   17) &quot;last-ok-ping-reply&quot;
   18) &quot;571&quot;
   19) &quot;last-ping-reply&quot;
   20) &quot;571&quot;
   21) &quot;down-after-milliseconds&quot;
   22) &quot;30000&quot;
   23) &quot;last-hello-message&quot;
   24) &quot;1043&quot;
   25) &quot;voted-leader&quot;
   26) &quot;?&quot;
   27) &quot;voted-leader-epoch&quot;
   28) &quot;0&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>sentinel sentinels master-name

</code></pre>
<h4><strong>检查可用 Sentinel 的数量</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel ckquorum mymaster
OK 2 usable Sentinels. Quorum and failover authorization can be reached

</code></pre>
<p>有两个可用的 Sentinel，可用完成仲裁和故障转移授权。</p>
<p>相关语法：</p>
<pre><code>sentinel ckquorum master-name

</code></pre>
<h4><strong>强制故障转移</strong></h4>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel failover mymaster
OK

</code></pre>
<p>相关语法：</p>
<pre><code>sentinel failover master-name

</code></pre>
<h3>在线修改配置信息</h3>
<p>在 Redis 2.8.4 之前如果需要修改 Sentinel 的配置文件，例如添加或删除一个监视主节点，需要先停止 Sentinel 服务，再找到配置文件修改之后，重新启动 Sentinel 才行，这样就给我们带来了很多的不便，尤其是生产环境的 Sentinel，正常情况下如果是非致命问题我们是不能手动停止服务的，幸运的是 Redis 2.8.4 之后，我们可以不停机在线修改配置文件了，修改命令有以下几个。</p>
<h4><strong>增加监视主节点</strong></h4>
<p>使用 <code>sentinel monitor mymaster IP Port Quorum</code> 命令来添加监视主节点，如下命令所示：</p>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel monitor mymaster 127.0.0.1 6379 2
OK

</code></pre>
<p>OK 表示添加监视主节点成功。</p>
<h4><strong>移除主节点的监视</strong></h4>
<p>使用 <code>sentinel remove master-name</code> 命令来实现移除主节点的监视，如下命令所示：</p>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel remove mymaster
OK

</code></pre>
<p>OK 表示操作成功。</p>
<h4><strong>修改 quorum 参数</strong></h4>
<p>使用 <code>sentinel set master-name quorum n</code> 来修改 quorum 参数，如下命令所示：</p>
<pre><code class="language-shell">127.0.0.1:26379&gt; sentinel set mymaster quorum 1
OK

</code></pre>
<p>quorum 参数用来表示确认主节点下线的 Sentinel 数量，如果 quorum 设置为 1 表示只要有一台 Sentinel 确认主观下线后，这个主节点就客观（真正地）下线了。</p>
<blockquote>
<p>小贴士：以上所有对配置文件的修改，都会自动被刷新到物理配置文件 sentinel.conf 中。</p>
</blockquote>
<h3>代码实战</h3>
<p>本文我们通过 Java 代码来实现，通过 Sentinel 连接信息获取相关 Redis 客户端，再进行相关 Redis 操作，这样 Sentinel 就会帮我们做容灾恢复，我们就不用担心操作某一个 Redis 服务器端，因为服务器挂了之后就会导致程序不可用了，具体实现代码如下：</p>
<pre><code class="language-java">import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisSentinelPool;
import utils.Config;

import java.util.HashSet;
import java.util.Set;

public class SentinelExample {
    // master name
    private static String _MASTER_NAME = &quot;mymaster&quot;;

    public static void main(String[] args) {
        // Sentinel 配置信息
        Set&lt;String&gt; set = new HashSet&lt;&gt;();
        // 连接信息 ip:port
        set.add(&quot;127.0.0.1:26379&quot;);
        // 创建 Sentinel 连接池
        JedisSentinelPool jedisSentinel = new JedisSentinelPool(_MASTER_NAME,
                set, Config.REDIS_AUTH);
        // 获取 Redis 客户端
        Jedis jedis = jedisSentinel.getResource();
        // 设置元素
        String setRes = jedis.set(&quot;key&quot;, &quot;Hello, redis.&quot;);
        System.out.println(setRes);
        // 获取元素
        System.out.println(jedis.get(&quot;key&quot;));
    }
}

</code></pre>
<p>以上程序执行结果如下：</p>
<pre><code>OK
Hello, redis.

</code></pre>
<h3>小结</h3>
<p>本文我们讲了 Sentinel 相关的命令操作，主要是用于查询相关主从节点和其他 Sentinel 信息的，还可以执行强制故障转移等，我们还讲了 2.8.4 提供的在线修改 Sentinel 参数的三个方法，方便我们更好的使用 Sentinel，最后用代码实现了通过 Sentinel 获取主节点并进行 Redis 服务器操作的实例，这样就讲完整个 Sentinel 的介绍和应用。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="37&#32;实战：Redis哨兵模式（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="39&#32;实战：Redis&#32;集群模式（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a877ce370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
