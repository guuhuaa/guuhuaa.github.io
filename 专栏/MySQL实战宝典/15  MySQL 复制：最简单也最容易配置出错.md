<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15  MySQL 复制：最简单也最容易配置出错.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;从业务出发，开启海量&#32;MySQL&#32;架构设计.md">00 开篇词  从业务出发，开启海量 MySQL 架构设计.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;数字类型：避免自增踩坑.md">01  数字类型：避免自增踩坑.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;字符串类型：不能忽略的&#32;COLLATION.md">02  字符串类型：不能忽略的 COLLATION.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;日期类型：TIMESTAMP&#32;可能是巨坑.md">03  日期类型：TIMESTAMP 可能是巨坑.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;非结构存储：用好&#32;JSON&#32;这张牌.md">04  非结构存储：用好 JSON 这张牌.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;表结构设计：忘记范式准则.md">05  表结构设计：忘记范式准则.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;表压缩：不仅仅是空间压缩.md">06  表压缩：不仅仅是空间压缩.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;表的访问设计：你该选择&#32;SQL&#32;还是&#32;NoSQL？.md">07  表的访问设计：你该选择 SQL 还是 NoSQL？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;索引：排序的艺术.md">08  索引：排序的艺术.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;索引组织表：万物皆索引.md">09  索引组织表：万物皆索引.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;组合索引：用好，性能提升&#32;10&#32;倍！.md">10  组合索引：用好，性能提升 10 倍！.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;索引出错：请理解&#32;CBO&#32;的工作原理.md">11  索引出错：请理解 CBO 的工作原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;JOIN&#32;连接：到底能不能写&#32;JOIN？.md">12  JOIN 连接：到底能不能写 JOIN？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;子查询：放心地使用子查询功能吧！.md">13  子查询：放心地使用子查询功能吧！.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;分区表：哪些场景我不建议用分区表？.md">14  分区表：哪些场景我不建议用分区表？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="15&#32;&#32;MySQL&#32;复制：最简单也最容易配置出错.md">15  MySQL 复制：最简单也最容易配置出错.md</a>
                    

                </li>
                <li>

                    
                    <a href="16&#32;&#32;读写分离设计：复制延迟？其实是你用错了.md">16  读写分离设计：复制延迟？其实是你用错了.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;高可用设计：你怎么活用三大架构方案？.md">17  高可用设计：你怎么活用三大架构方案？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;金融级高可用架构：必不可少的数据核对.md">18  金融级高可用架构：必不可少的数据核对.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;高可用套件：选择这么多，你该如何选？.md">19  高可用套件：选择这么多，你该如何选？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;InnoDB&#32;Cluster：改变历史的新产品.md">20  InnoDB Cluster：改变历史的新产品.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;数据库备份：备份文件也要检查！.md">21  数据库备份：备份文件也要检查！.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;分布式数据库架构：彻底理解什么叫分布式数据库.md">22  分布式数据库架构：彻底理解什么叫分布式数据库.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;分布式数据库表结构设计：如何正确地将数据分片？.md">23  分布式数据库表结构设计：如何正确地将数据分片？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;分布式数据库索引设计：二级索引、全局索引的最佳设计实践.md">24  分布式数据库索引设计：二级索引、全局索引的最佳设计实践.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;分布式数据库架构选型：分库分表&#32;or&#32;中间件&#32;？.md">25  分布式数据库架构选型：分库分表 or 中间件 ？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;分布式设计之禅：全链路的条带化设计.md">26  分布式设计之禅：全链路的条带化设计.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;分布式事务：我们到底要不要使用&#32;2PC？.md">27  分布式事务：我们到底要不要使用 2PC？.md</a>

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
                        <div><h1>15  MySQL 复制：最简单也最容易配置出错</h1>
<p>从今天开始，我们正式进入高可用架构的设计环节。</p>
<p>在前两个模块中，我们学习了 MySQL 架构中的表结构设计、索引设计。对业务开发的同学来说，掌握这些内容已经能很好地面向业务逻辑进行编码工作了。</p>
<p>但是业务需要上线，所以除了表和索引的结构设计之外，你还要做好高可用的设计。因为在真实的生产环境下，如果发生物理硬件故障，没有搭建高可用架构，会导致业务完全不可用。</p>
<p>而这在海量并发访问的互联网业务中完全不敢想象。所以除了业务架构，还要做好可用性的架构设计。</p>
<p>这一讲，我们就来学习 MySQL 高可用架构中最基础、最为核心的内容：MySQL 复制（Replication）。</p>
<h3>MySQL 复制架构</h3>
<p>数据库复制本质上就是数据同步。MySQL 数据库是基于二进制日志（binary log）进行数据增量同步，而二进制日志记录了所有对于 MySQL 数据库的修改操作。</p>
<p>在默认 ROW 格式二进制日志中，一条 SQL 操作影响的记录会被全部记录下来，比如一条 SQL语句更新了三行记录，在二进制日志中会记录被修改的这三条记录的前项（before image）和后项（after image）。</p>
<p>对于 INSERT 或 DELETE 操作，则会记录这条被插入或删除记录所有列的信息，我们来看一个例子：</p>
<pre><code>DELETE FROM orders_test 

WHERE o_orderdate = '1997-12-31';

Query OK, 2482 rows affected (0.07 sec)
</code></pre>
<p>可以看到，上面这条 SQL 执行的是删除操作，一共删除了有 2482 行记录。可以在 mysql 命令行下使用命令 SHOW BINLOG EVENTS 查看某个二进制日志文件的内容，比如上述删除操作发生在二进制日志文件 binlog.000004 中，你可以看到：</p>
<p><img src="assets/CioPOWDDJ7-ALugWAAFVUvkR12A461.png" alt="Drawing 0.png" /></p>
<p>通过 MySQL 数据库自带的命令 mysqlbinlog，可以解析二进制日志，观察到更为详细的每条记录的信息，比如：</p>
<p><img src="assets/Cgp9HWDDJ8SAdkn3AAHCe2DoWIw720.png" alt="Drawing 1.png" /></p>
<p>从图中，你可以通过二进制日志记录看到被删除记录的完整信息，还有每个列的属性，比如列的类型，是否允许为 NULL 值等。</p>
<p>如果是 UPDATE 操作，二进制日志中还记录了被修改记录完整的前项和后项，比如：</p>
<p><img src="assets/CioPOWDDJ8qAUjIpAAIxj14V0cE562.png" alt="Drawing 2.png" /></p>
<p>在有二进制日志的基础上，MySQL 数据库就可以通过数据复制技术实现数据同步了。而数据复制的本质就是把一台 MySQL 数据库上的变更同步到另一台 MySQL 数据库上。<strong>下面这张图显示了当前 MySQL 数据库的复制架构</strong>：</p>
<p><img src="assets/CioPOWDDJ8-ALENTAADSwBdKoIk997.png" alt="Drawing 3.png" /></p>
<p>可以看到，在 MySQL 复制中，一台是数据库的角色是 Master（也叫 Primary），剩下的服务器角色是 Slave（也叫 Standby）：</p>
<ul>
<li>Master 服务器会把数据变更产生的二进制日志通过 Dump 线程发送给 Slave 服务器；</li>
<li>Slave 服务器中的 I/O 线程负责接受二进制日志，并保存为中继日志；</li>
<li>SQL/Worker 线程负责并行执行中继日志，即在 Slave 服务器上回放 Master 产生的日志。</li>
</ul>
<p>得益于二进制日志，MySQL 的复制相比其他数据库，如 Oracle、PostgreSQL 等，非常灵活，用户可以根据自己的需要构建所需要的复制拓扑结构，比如：</p>
<p><img src="assets/Cgp9HWDDJ9WAajowAABzC8-hoJA062.png" alt="Drawing 4.png" /></p>
<p>在上图中，Slave1、Slave2、Slave3 都是 Master 的从服务器，而 Slave11 是 Slave1 的从服务器，Slave1 服务器既是 Master 的从机，又是 Slave11 的主机，所以 Slave1 是个级联的从机。同理，Slave3 也是台级联的从机。</p>
<p>在了解完复制的基本概念后，我们继续看如何配置 MySQL 的复制吧。</p>
<h3>MySQL 复制配置</h3>
<p>搭建 MySQL 复制实现非常简单，基本步骤如下：</p>
<ol>
<li>创建复制所需的账号和权限；</li>
<li>从 Master 服务器拷贝一份数据，可以使用逻辑备份工具 mysqldump、mysqlpump，或物理备份工具 Clone Plugin；</li>
<li>通过命令 CHANGE MASTER TO 搭建复制关系；</li>
<li>通过命令 SHOW SLAVE STATUS 观察复制状态。</li>
</ol>
<p>虽然 MySQL 复制原理和实施非常简单，但在配置时却容易出错，请你务必在配置文件中设置如下配置：</p>
<pre><code>gtid_mode = on

enforce_gtid_consistency = 1

binlog_gtid_simple_recovery = 1

relay_log_recovery = ON

master_info_repository = TABLE 

relay_log_info_repository = TABLE
</code></pre>
<p>上述设置都是用于保证 crash safe，即无论 Master 还是 Slave 宕机，当它们恢复后，连上主机后，主从数据依然一致，不会产生任何不一致的问题。</p>
<p>我经常听有同学反馈：MySQL会存在主从数据不一致的情况，<strong>请确认上述参数都已配置，否则任何的不一致都不是 MySQL 的问题，而是你使用 MySQL 的错误姿势所致</strong>。</p>
<p>了解完复制的配置后，我们接下来看一下 MySQL 支持的复制类型。</p>
<h3>MySQL复制类型及应用选项</h3>
<p>MySQL 复制可以分为以下几种类型：</p>
<p><img src="assets/CioPOWDDJ_aAMeY1AABfASRi428523.png" alt="Drawing 5.png" /></p>
<p>默认的复制是异步复制，而很多新同学因为不了解 MySQL 除了异步复制还有其他复制的类型，所以错误地在业务中使用了异步复制。为了解决这个问题，我们一起详细了解一下每种复制类型，以及它们在业务中的选型，方便你在业务做正确的选型。</p>
<h4>异步复制</h4>
<p>在异步复制（async replication）中，Master 不用关心 Slave 是否接收到二进制日志，所以 Master 与 Slave 没有任何的依赖关系。你可以认为 Master 和 Slave 是分别独自工作的两台服务器，数据最终会通过二进制日志达到一致。</p>
<p>异步复制的性能最好，因为它对数据库本身几乎没有任何开销，除非主从延迟非常大，Dump Thread 需要读取大量二进制日志文件。</p>
<p>如果业务对于数据一致性要求不高，当发生故障时，能容忍数据的丢失，甚至大量的丢失，推荐用异步复制，这样性能最好（比如像微博这样的业务，虽然它对性能的要求极高，但对于数据丢失，通常可以容忍）。但往往核心业务系统最关心的就是数据安全，比如监控业务、告警系统。</p>
<h4>半同步复制</h4>
<p>半同步复制要求 Master 事务提交过程中，至少有 N 个 Slave 接收到二进制日志，这样就能保证当 Master 发生宕机，至少有 N 台 Slave 服务器中的数据是完整的。</p>
<p>半同步复制并不是 MySQL 内置的功能，而是要安装半同步插件，并启用半同步复制功能，设置 N 个 Slave 接受二进制日志成功，比如：</p>
<pre><code>plugin-load=&quot;rpl_semi_sync_master=semisync_master.so;rpl_semi_sync_slave=semisync_slave.so&quot;

rpl-semi-sync-master-enabled = 1

rpl-semi-sync-slave-enabled = 1

rpl_semi_sync_master_wait_no_slave = 1
</code></pre>
<p>上面的配置中：</p>
<ul>
<li>第 1 行要求数据库启动时安装半同步插件；</li>
<li>第 2、3 行表示分别启用半同步 Master 和半同步 Slave 插件；</li>
<li>第 4 行表示半同步复制过程中，提交的事务必须至少有一个 Slave 接收到二进制日志。</li>
</ul>
<p>在半同步复制中，有损半同步复制是 MySQL 5.7 版本前的半同步复制机制，这种半同步复制在Master 发生宕机时，<strong>Slave 会丢失最后一批提交的数据</strong>，若这时 Slave 提升（Failover）为Master，可能会发生已经提交的事情不见了，发生了回滚的情况。</p>
<p>有损半同步复制原理如下图所示：</p>
<p><img src="assets/Cgp9HWDDKAWAS2YNAACrlAHSwSA608.png" alt="Drawing 6.png" /></p>
<p>可以看到，有损半同步是在 Master 事务提交后，即步骤 4 后，等待 Slave 返回 ACK，表示至少有 Slave 接收到了二进制日志，如果这时二进制日志还未发送到 Slave，Master 就发生宕机，则此时 Slave 就会丢失 Master 已经提交的数据。</p>
<p>而 MySQL 5.7 的无损半同步复制解决了这个问题，其原理如下图所示：</p>
<p><img src="assets/CioPOWDDKAqAHHU9AADAKTzSR4Y264.png" alt="Drawing 7.png" /></p>
<p>从上图可以看到，无损半同步复制 WAIT ACK 发生在事务提交之前，这样即便 Slave 没有收到二进制日志，但是 Master 宕机了，由于最后一个事务还没有提交，所以本身这个数据对外也不可见，不存在丢失的问题。</p>
<p>所以，对于任何有数据一致性要求的业务，如电商的核心订单业务、银行、保险、证券等与资金密切相关的业务，务必使用无损半同步复制。这样数据才是安全的、有保障的、即使发生宕机，从机也有一份完整的数据。</p>
<h4>多源复制</h4>
<p>无论是异步复制还是半同步复制，都是 1 个 Master 对应 N 个 Slave。其实 MySQL 也支持 N 个 Master 对应 1 个 Slave，这种架构就称之为多源复制。</p>
<p>多源复制允许在不同 MySQL 实例上的数据同步到 1 台 MySQL 实例上，方便在 1 台 Slave 服务器上进行一些统计查询，如常见的 OLAP 业务查询。</p>
<p>多源复制的架构如下所示：</p>
<p><img src="assets/Cgp9HWDDKBSAa76pAACAyeJ3YuE843.png" alt="Drawing 8.png" /></p>
<p>上图显示了订单库、库存库、供应商库，通过多源复制同步到了一台 MySQL 实例上，接着就可以通过 MySQL 8.0 提供的复杂 SQL 能力，对业务进行深度的数据分析和挖掘。</p>
<h4>延迟复制</h4>
<p>前面介绍的复制架构，Slave 在接收二进制日志后会尽可能快地回放日志，这样是为了避免主从之间出现延迟。而延迟复制却允许Slave 延迟回放接收到的二进制日志，为了避免主服务器上的误操作，马上又同步到了从服务器，导致数据完全丢失。</p>
<p>我们可以通过以下命令设置延迟复制：</p>
<pre><code>CHANGE MASTER TO master_delay = 3600
</code></pre>
<p>这样就人为设置了 Slave 落后 Master 服务器1个小时。</p>
<p>延迟复制在数据库的备份架构设计中非常常见，比如可以设置一个延迟一天的延迟备机，这样本质上说，用户可以有 1 份 24 小时前的快照。</p>
<p>那么当线上发生误操作，如 DROP TABLE、DROP DATABASE 这样灾难性的命令时，用户有一个 24 小时前的快照，数据可以快速恢复。</p>
<p>对金融行业来说，延迟复制是你备份设计中，必须考虑的一个架构部分。</p>
<h3>总结</h3>
<p>相信学完今天的内容，你一定会对 MySQL 复制技术有一个清晰的了解，认识到<strong>复制是数据同步的基础，而二进制日志就是复制的基石</strong>。我总结一下今天的重点：</p>
<ol>
<li>二进制日志记录了所有对于 MySQL 变更的操作；</li>
<li>可以通过命令 SHOW BINLOG EVENTS IN ... FROM ... 查看二进制日志的基本信息；</li>
<li>可以通过工具 mysqlbinlog 查看二进制日志的详细内容；</li>
<li><strong>复制搭建虽然简单，但别忘记配置 crash safe 相关参数</strong>，否则可能导致主从数据不一致；</li>
<li>异步复制用于非核心业务场景，不要求数据一致性；</li>
<li>无损半同步复制用于核心业务场景，如银行、保险、证券等核心业务，需要严格保障数据一致性；</li>
<li>多源复制可将多个 Master 数据汇总到一个数据库示例进行分析；</li>
<li>延迟复制主要用于误操作防范，金融行业要特别考虑这样的场景。</li>
</ol>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;&#32;分区表：哪些场景我不建议用分区表？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;&#32;读写分离设计：复制延迟？其实是你用错了.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43483c3c9c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/MySQL%E5%AE%9E%E6%88%98%E5%AE%9D%E5%85%B8/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
