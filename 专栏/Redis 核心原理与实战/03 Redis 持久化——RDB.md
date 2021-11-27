<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03 Redis 持久化——RDB.md</title>
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

                    <a class="current-tab" href="03&#32;Redis&#32;持久化——RDB.md">03 Redis 持久化——RDB.md</a>
                    

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
                        <div><h1>03 Redis 持久化——RDB</h1>
<blockquote>
<p>Redis 的读写都是在内存中，所以它的性能较高，但在内存中的数据会随着服务器的重启而丢失，为了保证数据不丢失，我们需要将内存中的数据存储到磁盘，以便 Redis 重启时能够从磁盘中恢复原有的数据，而整个过程就叫做 Redis 持久化。</p>
</blockquote>
<p><img src="assets/2020-02-24-122623.png" alt="image.png" /> Redis 持久化也是 Redis 和 Memcached 的主要区别之一，因为 Memcached 不具备持久化功能。</p>
<h3>1 持久化的几种方式</h3>
<p>Redis 持久化拥有以下三种方式：</p>
<ul>
<li><strong>快照方式</strong>（RDB, Redis DataBase）将某一个时刻的内存数据，以二进制的方式写入磁盘；</li>
<li><strong>文件追加方式</strong>（AOF, Append Only File），记录所有的操作命令，并以文本的形式追加到文件中；</li>
<li><strong>混合持久化方式</strong>，Redis 4.0 之后新增的方式，混合持久化是结合了 RDB 和 AOF 的优点，在写入的时候，先把当前的数据以 RDB 的形式写入文件的开头，再将后续的操作命令以 AOF 的格式存入文件，这样既能保证 Redis 重启时的速度，又能减低数据丢失的风险。</li>
</ul>
<p>因为每种持久化方案，都有特定的使用场景，让我们先从 RDB 持久化说起吧。</p>
<h3>2 RDB简介</h3>
<p>RDB（Redis DataBase）是将某一个时刻的内存快照（Snapshot），以二进制的方式写入磁盘的过程。</p>
<h3>3 持久化触发</h3>
<p>RDB 的持久化触发方式有两类：一类是手动触发，另一类是自动触发。</p>
<h4>1）手动触发</h4>
<p>手动触发持久化的操作有两个： <code>save</code> 和 <code>bgsave</code> ，它们主要区别体现在：是否阻塞 Redis 主线程的执行。</p>
<h5>① save 命令</h5>
<p>在客户端中执行 <code>save</code> 命令，就会触发 Redis 的持久化，但同时也是使 Redis 处于阻塞状态，直到 RDB 持久化完成，才会响应其他客户端发来的命令，所以<strong>在生产环境一定要慎用</strong>。</p>
<p><code>save</code> 命令使用如下： <img src="assets/2020-02-24-122625.png" alt="image.png" /> 从图片可以看出，当执行完 <code>save</code> 命令之后，持久化文件 <code>dump.rdb</code> 的修改时间就变了，这就表示 <code>save</code> 成功的触发了 RDB 持久化。 <code>save</code> 命令执行流程，如下图所示： <img src="assets/2020-02-24-122626.png" alt="image.png" /></p>
<h5>② bgsave 命令</h5>
<p>bgsave（background save）既后台保存的意思， 它和 <code>save</code> 命令最大的区别就是 <code>bgsave</code> 会 fork() 一个子进程来执行持久化，整个过程中只有在 fork() 子进程时有短暂的阻塞，当子进程被创建之后，Redis 的主进程就可以响应其他客户端的请求了，相对于整个流程都阻塞的 <code>save</code> 命令来说，显然 <code>bgsave</code> 命令更适合我们使用。 <code>bgsave</code> 命令使用，如下图所示： <img src="assets/2020-02-24-122627.png" alt="image.png" /> <code>bgsave</code> 执行流程，如下图所示： <img src="assets/2020-02-24-122628.png" alt="image.png" /></p>
<h4>2）自动触发</h4>
<p>说完了 RDB 的手动触发方式，下面来看如何自动触发 RDB 持久化？ RDB 自动持久化主要来源于以下几种情况。</p>
<h5>① save m n</h5>
<p><code>save m n</code> 是指在 m 秒内，如果有 n 个键发生改变，则自动触发持久化。 参数 m 和 n 可以在 Redis 的配置文件中找到，例如，<code>save 60 1</code> 则表明在 60 秒内，至少有一个键发生改变，就会触发 RDB 持久化。 自动触发持久化，本质是 Redis 通过判断，如果满足设置的触发条件，自动执行一次 <code>bgsave</code> 命令。 注意：当设置多个 save m n 命令时，满足任意一个条件都会触发持久化。 例如，我们设置了以下两个 save m n 命令：</p>
<ul>
<li>save 60 10</li>
<li>save 600 1</li>
</ul>
<p>当 60s 内如果有 10 次 Redis 键值发生改变，就会触发持久化；如果 60s 内 Redis 的键值改变次数少于 10 次，那么 Redis 就会判断 600s 内，Redis 的键值是否至少被修改了一次，如果满足则会触发持久化。</p>
<h5>② flushall</h5>
<p><code>flushall</code> 命令用于清空 Redis 数据库，在生产环境下一定慎用，当 Redis 执行了 <code>flushall</code> 命令之后，则会触发自动持久化，把 RDB 文件清空。 执行结果如下图所示： <img src="assets/2020-02-24-122629.png" alt="image.png" /></p>
<h5>③ 主从同步触发</h5>
<p>在 Redis 主从复制中，当从节点执行全量复制操作时，主节点会执行 <code>bgsave</code> 命令，并将 RDB 文件发送给从节点，该过程会自动触发 Redis 持久化。</p>
<h3>4 配置说明</h3>
<p>合理的设置 RDB 的配置，可以保障 Redis 高效且稳定的运行，下面一起来看 RDB 的配置项都有哪些？</p>
<p>RDB 配置参数可以在  Redis 的配置文件中找见，具体内容如下：</p>
<pre><code># RDB 保存的条件
save 900 1
save 300 10
save 60 10000

# bgsave 失败之后，是否停止持久化数据到磁盘，yes 表示停止持久化，no 表示忽略错误继续写文件。
stop-writes-on-bgsave-error yes

# RDB 文件压缩
rdbcompression yes

# 写入文件和读取文件时是否开启 RDB 文件检查，检查是否有无损坏，如果在启动是检查发现损坏，则停止启动。
rdbchecksum yes

# RDB 文件名
dbfilename dump.rdb

# RDB 文件目录
dir ./

</code></pre>
<p>其中比较重要的参数如下列表： <strong>① save 参数</strong> 它是用来配置触发 RDB 持久化条件的参数，满足保存条件时将会把数据持久化到硬盘。 默认配置说明如下：</p>
<ul>
<li>save 900 1：表示 900 秒内如果至少有 1 个 key 值变化，则把数据持久化到硬盘；</li>
<li>save 300 10：表示 300 秒内如果至少有 10 个 key 值变化，则把数据持久化到硬盘；</li>
<li>save 60 10000：表示 60 秒内如果至少有 10000 个 key 值变化，则把数据持久化到硬盘。</li>
</ul>
<p><strong>② rdbcompression 参数</strong> 它的默认值是 <code>yes</code> 表示开启 RDB 文件压缩，Redis 会采用 LZF 算法进行压缩。如果不想消耗 CPU 性能来进行文件压缩的话，可以设置为关闭此功能，这样的缺点是需要更多的磁盘空间来保存文件。 <strong>③ rdbchecksum 参数</strong> 它的默认值为 <code>yes</code> 表示写入文件和读取文件时是否开启 RDB 文件检查，检查是否有无损坏，如果在启动是检查发现损坏，则停止启动。</p>
<h3>5 配置查询</h3>
<p>Redis 中可以使用命令查询当前配置参数。查询命令的格式为：<code>config get xxx</code> ，例如，想要获取 RDB 文件的存储名称设置，可以使用 <code>config get dbfilename</code> ，执行效果如下图所示： <img src="assets/2020-02-24-122630.png" alt="image.png" /> 查询 RDB 的文件目录，可使用命令 <code>config get dir</code> ，执行效果如下图所示： <img src="assets/2020-02-24-122633.png" alt="image.png" /></p>
<h3>6 配置设置</h3>
<p>设置 RDB 的配置，可以通过以下两种方式：</p>
<ul>
<li>手动修改 Redis 配置文件；</li>
<li>使用命令行设置，例如，使用 <code>config set dir &quot;/usr/data&quot;</code> 就是用于修改 RDB 的存储目录。</li>
</ul>
<p><strong>注意</strong>：手动修改 Redis 配置文件的方式是全局生效的，即重启 Redis 服务器设置参数也不会丢失，而使用命令修改的方式，在 Redis 重启之后就会丢失。但手动修改 Redis 配置文件，想要立即生效需要重启 Redis 服务器，而命令的方式则不需要重启 Redis 服务器。</p>
<blockquote>
<p>小贴士：Redis 的配置文件位于 Redis 安装目录的根路径下，默认名称为 redis.conf。</p>
</blockquote>
<h3>7 RDB 文件恢复</h3>
<p>当 Redis 服务器启动时，如果 Redis 根目录存在 RDB 文件 dump.rdb，Redis 就会自动加载 RDB 文件恢复持久化数据。 如果根目录没有 dump.rdb 文件，请先将 dump.rdb 文件移动到 Redis 的根目录。 <strong>验证 RDB 文件是否被加载</strong> Redis 在启动时有日志信息，会显示是否加载了 RDB 文件，我们执行 Redis 启动命令：<code>src/redis-server redis.conf</code> ，如下图所示： <img src="assets/2020-02-24-122634.png" alt="image.png" /> 从日志上可以看出， Redis 服务在启动时已经正常加载了 RDB 文件。</p>
<blockquote>
<p>小贴士：Redis 服务器在载入 RDB 文件期间，会一直处于阻塞状态，直到载入工作完成为止。</p>
</blockquote>
<h3>8 RDB 优缺点</h3>
<h4>1）RDB 优点</h4>
<ul>
<li>RDB 的内容为二进制的数据，占用内存更小，更紧凑，更适合做为备份文件；</li>
<li>RDB 对灾难恢复非常有用，它是一个紧凑的文件，可以更快的传输到远程服务器进行 Redis 服务恢复；</li>
<li>RDB 可以更大程度的提高 Redis 的运行速度，因为每次持久化时 Redis 主进程都会 fork() 一个子进程，进行数据持久化到磁盘，Redis 主进程并不会执行磁盘 I/O 等操作；</li>
<li>与 AOF 格式的文件相比，RDB 文件可以更快的重启。</li>
</ul>
<h4>2）RDB 缺点</h4>
<ul>
<li>因为 RDB 只能保存某个时间间隔的数据，如果中途 Redis 服务被意外终止了，则会丢失一段时间内的 Redis 数据；</li>
<li>RDB 需要经常 fork() 才能使用子进程将其持久化在磁盘上。如果数据集很大，fork() 可能很耗时，并且如果数据集很大且 CPU 性能不佳，则可能导致 Redis 停止为客户端服务几毫秒甚至一秒钟。</li>
</ul>
<h3>9 禁用持久化</h3>
<p>禁用持久化可以提高 Redis 的执行效率，如果对数据丢失不敏感的情况下，可以在连接客户端的情况下，执行 <code>config set save &quot;&quot;</code> 命令即可禁用 Redis 的持久化，如下图所示： <img src="assets/2020-02-24-122636.png" alt="image.png" /></p>
<h3>10 小结</h3>
<p>通过本文我们可以得知，RDB 持久化分为手动触发和自动触发两种方式，它的优点是存储文件小，Redis 启动	时恢复数据比较快，缺点是有丢失数据的风险。RDB 文件的恢复也很简单，只需要把 RDB 文件放到 Redis 的根目录，在 Redis 启动时就会自动加载并恢复数据。 最后给大家留一个思考题：如果 Redis 服务器 CPU 占用过高，可能是什么原因导致的？欢迎各位在评论区，写下你们的答案。</p>
<p><strong>参考&amp;鸣谢</strong> <a href="https://redis.io/topics/persistence">https://redis.io/topics/persistence</a> <a href="https://blog.csdn.net/qq_36318234/article/details/79994133">https://blog.csdn.net/qq_36318234/article/details/79994133</a> <a href="https://www.cnblogs.com/ysocean/p/9114268.html">https://www.cnblogs.com/ysocean/p/9114268.html</a> <a href="https://www.cnblogs.com/wdliu/p/9377278.html">https://www.cnblogs.com/wdliu/p/9377278.html</a></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;Redis&#32;快速搭建与使用.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;Redis&#32;持久化——AOF.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4349ba9c4c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
