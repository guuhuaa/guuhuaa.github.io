<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>38  都说InnoDB好，那还要不要使用Memory引擎？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;这一次，让我们一起来搞懂MySQL.md">00 开篇词  这一次，让我们一起来搞懂MySQL.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;基础架构：一条SQL查询语句是如何执行的？.md">01  基础架构：一条SQL查询语句是如何执行的？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;日志系统：一条SQL更新语句是如何执行的？.md">02  日志系统：一条SQL更新语句是如何执行的？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;事务隔离：为什么你改了我还看不见？.md">03  事务隔离：为什么你改了我还看不见？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;深入浅出索引（上）.md">04  深入浅出索引（上）.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;深入浅出索引（下）.md">05  深入浅出索引（下）.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;全局锁和表锁&#32;：给表加个字段怎么有这么多阻碍？.md">06  全局锁和表锁 ：给表加个字段怎么有这么多阻碍？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;行锁功过：怎么减少行锁对性能的影响？.md">07  行锁功过：怎么减少行锁对性能的影响？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;事务到底是隔离的还是不隔离的？.md">08  事务到底是隔离的还是不隔离的？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;普通索引和唯一索引，应该怎么选择？.md">09  普通索引和唯一索引，应该怎么选择？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;MySQL为什么有时候会选错索引？.md">10  MySQL为什么有时候会选错索引？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;怎么给字符串字段加索引？.md">11  怎么给字符串字段加索引？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;为什么我的MySQL会“抖”一下？.md">12  为什么我的MySQL会“抖”一下？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;为什么表数据删掉一半，表文件大小不变？.md">13  为什么表数据删掉一半，表文件大小不变？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;count()这么慢，我该怎么办？.md">14  count()这么慢，我该怎么办？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;答疑文章（一）：日志和索引相关问题.md">15  答疑文章（一）：日志和索引相关问题.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;“order&#32;by”是怎么工作的？.md">16  “order by”是怎么工作的？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何正确地显示随机消息？.md">17  如何正确地显示随机消息？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;为什么这些SQL语句逻辑相同，性能却差异巨大？.md">18  为什么这些SQL语句逻辑相同，性能却差异巨大？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;为什么我只查一行的语句，也执行这么慢？.md">19  为什么我只查一行的语句，也执行这么慢？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;幻读是什么，幻读有什么问题？.md">20  幻读是什么，幻读有什么问题？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;为什么我只改一行的语句，锁这么多？.md">21  为什么我只改一行的语句，锁这么多？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;MySQL有哪些“饮鸩止渴”提高性能的方法？.md">22  MySQL有哪些“饮鸩止渴”提高性能的方法？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;MySQL是怎么保证数据不丢的？.md">23  MySQL是怎么保证数据不丢的？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;MySQL是怎么保证主备一致的？.md">24  MySQL是怎么保证主备一致的？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;MySQL是怎么保证高可用的？.md">25  MySQL是怎么保证高可用的？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;备库为什么会延迟好几个小时？.md">26  备库为什么会延迟好几个小时？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;主库出问题了，从库怎么办？.md">27  主库出问题了，从库怎么办？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;读写分离有哪些坑？.md">28  读写分离有哪些坑？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;如何判断一个数据库是不是出问题了？.md">29  如何判断一个数据库是不是出问题了？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;答疑文章（二）：用动态的观点看加锁.md">30  答疑文章（二）：用动态的观点看加锁.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;误删数据后除了跑路，还能怎么办？.md">31  误删数据后除了跑路，还能怎么办？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;为什么还有kill不掉的语句？.md">32  为什么还有kill不掉的语句？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;我查这么多数据，会不会把数据库内存打爆？.md">33  我查这么多数据，会不会把数据库内存打爆？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;到底可不可以使用join？.md">34  到底可不可以使用join？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;join语句怎么优化？.md">35  join语句怎么优化？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;为什么临时表可以重名？.md">36  为什么临时表可以重名？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;什么时候会使用内部临时表？.md">37  什么时候会使用内部临时表？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="38&#32;&#32;都说InnoDB好，那还要不要使用Memory引擎？.md">38  都说InnoDB好，那还要不要使用Memory引擎？.md</a>
                    

                </li>
                <li>

                    
                    <a href="39&#32;&#32;自增主键为什么不是连续的？.md">39  自增主键为什么不是连续的？.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;insert语句的锁为什么这么多？.md">40  insert语句的锁为什么这么多？.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;怎么最快地复制一张表？.md">41  怎么最快地复制一张表？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;grant之后要跟着flush&#32;privileges吗？.md">42  grant之后要跟着flush privileges吗？.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;要不要使用分区表？.md">43  要不要使用分区表？.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;答疑文章（三）：说一说这些好问题.md">44  答疑文章（三）：说一说这些好问题.md</a>

                </li>
                <li>

                    
                    <a href="45&#32;&#32;自增id用完怎么办？.md">45  自增id用完怎么办？.md</a>

                </li>
                <li>

                    
                    <a href="我的MySQL心路历程.md">我的MySQL心路历程.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;点线网面，一起构建MySQL知识网络.md">结束语  点线网面，一起构建MySQL知识网络.md</a>

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
                        <div><h1>38  都说InnoDB好，那还要不要使用Memory引擎？</h1>
<p>我在上一篇文章末尾留给你的问题是：两个 group by 语句都用了 order by null，为什么使用内存临时表得到的语句结果里，0 这个值在最后一行；而使用磁盘临时表得到的结果里，0 这个值在第一行？</p>
<p>今天我们就来看看，出现这个问题的原因吧。</p>
<h1>内存表的数据组织结构</h1>
<p>为了便于分析，我来把这个问题简化一下，假设有以下的两张表 t1 和 t2，其中表 t1 使用 Memory 引擎， 表 t2 使用 InnoDB 引擎。</p>
<pre><code>create table t1(id int primary key, c int) engine=Memory;
create table t2(id int primary key, c int) engine=innodb;
insert into t1 values(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(0,0);
insert into t2 values(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(0,0);
</code></pre>
<p>然后，我分别执行 select * from t1 和 select * from t2。</p>
<p><img src="assets/3fb1100b6e3390357d4efff0ba4765e6.png" alt="img" /></p>
<p>图 1 两个查询结果 -0 的位置</p>
<p>可以看到，内存表 t1 的返回结果里面 0 在最后一行，而 InnoDB 表 t2 的返回结果里 0 在第一行。</p>
<p>出现这个区别的原因，要从这两个引擎的主键索引的组织方式说起。</p>
<p>表 t2 用的是 InnoDB 引擎，它的主键索引 id 的组织方式，你已经很熟悉了：InnoDB 表的数据就放在主键索引树上，主键索引是 B+ 树。所以表 t2 的数据组织方式如下图所示：</p>
<p><img src="assets/4e29e4f9db55ace6ab09161c68ad8c8d.jpg" alt="img" /></p>
<p>图 2 表 t2 的数据组织</p>
<p>主键索引上的值是有序存储的。在执行 select * 的时候，就会按照叶子节点从左到右扫描，所以得到的结果里，0 就出现在第一行。</p>
<p>与 InnoDB 引擎不同，Memory 引擎的数据和索引是分开的。我们来看一下表 t1 中的数据内容。</p>
<p><img src="assets/dde03e92074cecba4154d30cd16a9684.jpg" alt="img" /></p>
<p>图 3 表 t1 的数据组织</p>
<p>可以看到，内存表的数据部分以数组的方式单独存放，而主键 id 索引里，存的是每个数据的位置。主键 id 是 hash 索引，可以看到索引上的 key 并不是有序的。</p>
<p>在内存表 t1 中，当我执行 select * 的时候，走的是全表扫描，也就是顺序扫描这个数组。因此，0 就是最后一个被读到，并放入结果集的数据。</p>
<p>可见，InnoDB 和 Memory 引擎的数据组织方式是不同的：</p>
<ul>
<li>InnoDB 引擎把数据放在主键索引上，其他索引上保存的是主键 id。这种方式，我们称之为<strong>索引组织表</strong>（Index Organizied Table）。</li>
<li>而 Memory 引擎采用的是把数据单独存放，索引上保存数据位置的数据组织形式，我们称之为<strong>堆组织表</strong>（Heap Organizied Table）。</li>
</ul>
<p>从中我们可以看出，这两个引擎的一些典型不同：</p>
<ol>
<li>InnoDB 表的数据总是有序存放的，而内存表的数据就是按照写入顺序存放的；</li>
<li>当数据文件有空洞的时候，InnoDB 表在插入新数据的时候，为了保证数据有序性，只能在固定的位置写入新值，而内存表找到空位就可以插入新值；</li>
<li>数据位置发生变化的时候，InnoDB 表只需要修改主键索引，而内存表需要修改所有索引；</li>
<li>InnoDB 表用主键索引查询时需要走一次索引查找，用普通索引查询的时候，需要走两次索引查找。而内存表没有这个区别，所有索引的“地位”都是相同的。</li>
<li>InnoDB 支持变长数据类型，不同记录的长度可能不同；内存表不支持 Blob 和 Text 字段，并且即使定义了 varchar(N)，实际也当作 char(N)，也就是固定长度字符串来存储，因此内存表的每行数据长度相同。</li>
</ol>
<p>由于内存表的这些特性，每个数据行被删除以后，空出的这个位置都可以被接下来要插入的数据复用。比如，如果要在表 t1 中执行：</p>
<pre><code>delete from t1 where id=5;
insert into t1 values(10,10);
select * from t1;
</code></pre>
<p>就会看到返回结果里，id=10 这一行出现在 id=4 之后，也就是原来 id=5 这行数据的位置。</p>
<p>需要指出的是，表 t1 的这个主键索引是哈希索引，因此如果执行范围查询，比如</p>
<pre><code>select * from t1 where id&lt;5;
</code></pre>
<p>是用不上主键索引的，需要走全表扫描。你可以借此再回顾下[第 4 篇文章]的内容。那如果要让内存表支持范围扫描，应该怎么办呢 ？</p>
<h1>hash 索引和 B-Tree 索引</h1>
<p>实际上，内存表也是支 B-Tree 索引的。在 id 列上创建一个 B-Tree 索引，SQL 语句可以这么写：</p>
<pre><code>alter table t1 add index a_btree_index using btree (id);
</code></pre>
<p>这时，表 t1 的数据组织形式就变成了这样：</p>
<p><img src="assets/1788deca56cb83c114d8353c92e3bde3.jpg" alt="img" /></p>
<p>图 4 表 t1 的数据组织 -- 增加 B-Tree 索引</p>
<p>新增的这个 B-Tree 索引你看着就眼熟了，这跟 InnoDB 的 b+ 树索引组织形式类似。</p>
<p>作为对比，你可以看一下这下面这两个语句的输出：</p>
<p><img src="assets/a85808fcccab24911d257d720550328a.png" alt="img" /></p>
<p>图 5 使用 B-Tree 和 hash 索引查询返回结果对比</p>
<p>可以看到，执行 select * from t1 where id&lt;5 的时候，优化器会选择 B-Tree 索引，所以返回结果是 0 到 4。 使用 force index 强行使用主键 id 这个索引，id=0 这一行就在结果集的最末尾了。</p>
<p>其实，一般在我们的印象中，内存表的优势是速度快，其中的一个原因就是 Memory 引擎支持 hash 索引。当然，更重要的原因是，内存表的所有数据都保存在内存，而内存的读写速度总是比磁盘快。</p>
<p>但是，接下来我要跟你说明，为什么我不建议你在生产环境上使用内存表。这里的原因主要包括两个方面：</p>
<ol>
<li>锁粒度问题；</li>
<li>数据持久化问题。</li>
</ol>
<h1>内存表的锁</h1>
<p>我们先来说说内存表的锁粒度问题。</p>
<p>内存表不支持行锁，只支持表锁。因此，一张表只要有更新，就会堵住其他所有在这个表上的读写操作。</p>
<p>需要注意的是，这里的表锁跟之前我们介绍过的 MDL 锁不同，但都是表级的锁。接下来，我通过下面这个场景，跟你模拟一下内存表的表级锁。</p>
<p><img src="assets/f216e2d707559ed2ca98fbe21e509f29.png" alt="img" /></p>
<p>图 6 内存表的表锁 -- 复现步骤</p>
<p>在这个执行序列里，session A 的 update 语句要执行 50 秒，在这个语句执行期间 session B 的查询会进入锁等待状态。session C 的 show processlist 结果输出如下：</p>
<p><img src="assets/14d88076dad6db573f0b66f2c17df916.png" alt="img" /></p>
<p>图 7 内存表的表锁 -- 结果</p>
<p>跟行锁比起来，表锁对并发访问的支持不够好。所以，内存表的锁粒度问题，决定了它在处理并发事务的时候，性能也不会太好。</p>
<h1>数据持久性问题</h1>
<p>接下来，我们再看看数据持久性的问题。</p>
<p>数据放在内存中，是内存表的优势，但也是一个劣势。因为，数据库重启的时候，所有的内存表都会被清空。</p>
<p>你可能会说，如果数据库异常重启，内存表被清空也就清空了，不会有什么问题啊。但是，在高可用架构下，内存表的这个特点简直可以当做 bug 来看待了。为什么这么说呢？</p>
<p><strong>我们先看看 M-S 架构下，使用内存表存在的问题。</strong></p>
<p><img src="assets/5b910e4c0f1afa219aeecd1f291c95e9.jpg" alt="img" /></p>
<p>图 8 M-S 基本架构</p>
<p>我们来看一下下面这个时序：</p>
<ol>
<li>业务正常访问主库；</li>
<li>备库硬件升级，备库重启，内存表 t1 内容被清空；</li>
<li>备库重启后，客户端发送一条 update 语句，修改表 t1 的数据行，这时备库应用线程就会报错“找不到要更新的行”。</li>
</ol>
<p>这样就会导致主备同步停止。当然，如果这时候发生主备切换的话，客户端会看到，表 t1 的数据“丢失”了。</p>
<p>在图 8 中这种有 proxy 的架构里，大家默认主备切换的逻辑是由数据库系统自己维护的。这样对客户端来说，就是“网络断开，重连之后，发现内存表数据丢失了”。</p>
<p>你可能说这还好啊，毕竟主备发生切换，连接会断开，业务端能够感知到异常。</p>
<p>但是，接下来内存表的这个特性就会让使用现象显得更“诡异”了。由于 MySQL 知道重启之后，内存表的数据会丢失。所以，担心主库重启之后，出现主备不一致，MySQL 在实现上做了这样一件事儿：在数据库重启之后，往 binlog 里面写入一行 DELETE FROM t1。</p>
<p><strong>如果你使用是如图 9 所示的双 M 结构的话：</strong></p>
<p><img src="assets/4089c9c1f92ce61d2ed779fd0932ba57.jpg" alt="img" /></p>
<p>图 9 双 M 结构</p>
<p>在备库重启的时候，备库 binlog 里的 delete 语句就会传到主库，然后把主库内存表的内容删除。这样你在使用的时候就会发现，主库的内存表数据突然被清空了。</p>
<p>基于上面的分析，你可以看到，内存表并不适合在生产环境上作为普通数据表使用。</p>
<p>有同学会说，但是内存表执行速度快呀。这个问题，其实你可以这么分析：</p>
<ol>
<li>如果你的表更新量大，那么并发度是一个很重要的参考指标，InnoDB 支持行锁，并发度比内存表好；</li>
<li>能放到内存表的数据量都不大。如果你考虑的是读的性能，一个读 QPS 很高并且数据量不大的表，即使是使用 InnoDB，数据也是都会缓存在 InnoDB Buffer Pool 里的。因此，使用 InnoDB 表的读性能也不会差。</li>
</ol>
<p>所以，**我建议你把普通内存表都用 InnoDB 表来代替。**但是，有一个场景却是例外的。</p>
<p>这个场景就是，我们在第 35 和 36 篇说到的用户临时表。在数据量可控，不会耗费过多内存的情况下，你可以考虑使用内存表。</p>
<p>内存临时表刚好可以无视内存表的两个不足，主要是下面的三个原因：</p>
<ol>
<li>临时表不会被其他线程访问，没有并发性的问题；</li>
<li>临时表重启后也是需要删除的，清空数据这个问题不存在；</li>
<li>备库的临时表也不会影响主库的用户线程。</li>
</ol>
<p>现在，我们回过头再看一下第 35 篇 join 语句优化的例子，当时我建议的是创建一个 InnoDB 临时表，使用的语句序列是：</p>
<pre><code>create temporary table temp_t(id int primary key, a int, b int, index(b))engine=innodb;
insert into temp_t select * from t2 where b&gt;=1 and b&lt;=2000;
select * from t1 join temp_t on (t1.b=temp_t.b);
</code></pre>
<p>了解了内存表的特性，你就知道了， 其实这里使用内存临时表的效果更好，原因有三个：</p>
<ol>
<li>相比于 InnoDB 表，使用内存表不需要写磁盘，往表 temp_t 的写数据的速度更快；</li>
<li>索引 b 使用 hash 索引，查找的速度比 B-Tree 索引快；</li>
<li>临时表数据只有 2000 行，占用的内存有限。</li>
</ol>
<p>因此，你可以对[第 35 篇文章]的语句序列做一个改写，将临时表 t1 改成内存临时表，并且在字段 b 上创建一个 hash 索引。</p>
<pre><code>create temporary table temp_t(id int primary key, a int, b int, index (b))engine=memory;
insert into temp_t select * from t2 where b&gt;=1 and b&lt;=2000;
select * from t1 join temp_t on (t1.b=temp_t.b);
</code></pre>
<p><img src="assets/a468ba6d14ea225623074b6255b99f92.png" alt="img" /></p>
<p>图 10 使用内存临时表的执行效果</p>
<p>可以看到，不论是导入数据的时间，还是执行 join 的时间，使用内存临时表的速度都比使用 InnoDB 临时表要更快一些。</p>
<h1>小结</h1>
<p>今天这篇文章，我从“要不要使用内存表”这个问题展开，和你介绍了 Memory 引擎的几个特性。</p>
<p>可以看到，由于重启会丢数据，如果一个备库重启，会导致主备同步线程停止；如果主库跟这个备库是双 M 架构，还可能导致主库的内存表数据被删掉。</p>
<p>因此，在生产上，我不建议你使用普通内存表。</p>
<p>如果你是 DBA，可以在建表的审核系统中增加这类规则，要求业务改用 InnoDB 表。我们在文中也分析了，其实 InnoDB 表性能还不错，而且数据安全也有保障。而内存表由于不支持行锁，更新语句会阻塞查询，性能也未必就如想象中那么好。</p>
<p>基于内存表的特性，我们还分析了它的一个适用场景，就是内存临时表。内存表支持 hash 索引，这个特性利用起来，对复杂查询的加速效果还是很不错的。</p>
<p>最后，我给你留一个问题吧。</p>
<p>假设你刚刚接手的一个数据库上，真的发现了一个内存表。备库重启之后肯定是会导致备库的内存表数据被清空，进而导致主备同步停止。这时，最好的做法是将它修改成 InnoDB 引擎表。</p>
<p>假设当时的业务场景暂时不允许你修改引擎，你可以加上什么自动化逻辑，来避免主备同步停止呢？</p>
<p>你可以把你的思考和分析写在评论区，我会在下一篇文章的末尾跟你讨论这个问题。感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="37&#32;&#32;什么时候会使用内部临时表？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="39&#32;&#32;自增主键为什么不是连续的？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4347b3afc170ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/MySQL%E5%AE%9E%E6%88%9845%E8%AE%B2/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
