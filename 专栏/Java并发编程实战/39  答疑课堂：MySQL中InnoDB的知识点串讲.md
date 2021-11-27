<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>39  答疑课堂：MySQL中InnoDB的知识点串讲.md</title>
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

                    
                    <a href="32&#32;&#32;MySQL调优之SQL语句：如何写出高性能SQL语句？.md">32  MySQL调优之SQL语句：如何写出高性能SQL语句？.md</a>

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

                    <a class="current-tab" href="39&#32;&#32;答疑课堂：MySQL中InnoDB的知识点串讲.md">39  答疑课堂：MySQL中InnoDB的知识点串讲.md</a>
                    

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
                        <div><h1>39  答疑课堂：MySQL中InnoDB的知识点串讲</h1>
<p>你好，我是刘超。</p>
<p>模块六有关数据库调优的内容到本周也正式结束了，今天我们一起串下 MySQL 中 InnoDB 的知识点。InnoDB 存储引擎作为我们最常用到的存储引擎之一，充分熟悉它的的实现和运行原理，有助于我们更好地创建和维护数据库表。</p>
<h2>InnoDB 体系架构</h2>
<p>InnoDB 主要包括了内存池、后台线程以及存储文件。内存池又是由多个内存块组成的，主要包括缓存磁盘数据、redo log 缓冲等；后台线程则包括了 Master Thread、IO Thread 以及 Purge Thread 等；由 InnoDB 存储引擎实现的表的存储结构文件一般包括表结构文件（.frm）、共享表空间文件（ibdata1）、独占表空间文件（ibd）以及日志文件（redo 文件等）等。</p>
<p><img src="assets/f26b2fad64a9a527b5ac0e8c7f4be992.jpg" alt="img" /></p>
<h3>1. 内存池</h3>
<p>我们知道，如果客户端从数据库中读取数据是直接从磁盘读取的话，无疑会带来一定的性能瓶颈，缓冲池的作用就是提高整个数据库的读写性能。</p>
<p>客户端读取数据时，如果数据存在于缓冲池中，客户端就会直接读取缓冲池中的数据，否则再去磁盘中读取；对于数据库中的修改数据，首先是修改在缓冲池中的数据，然后再通过 Master Thread 线程刷新到磁盘上。</p>
<p>理论上来说，缓冲池的内存越大越好。我们在[第 38 讲]中详细讲过了缓冲池的大小配置方式以及调优。</p>
<p>缓冲池中不仅缓存索引页和数据页，还包括了 undo 页，插入缓存、自适应哈希索引以及 InnoDB 的锁信息等等。</p>
<p>InnoDB 允许多个缓冲池实例，从而减少数据库内部资源的竞争，增强数据库的并发处理能力，[第 38 讲]还讲到了缓冲池实例的配置以及调优。</p>
<p>InnoDB 存储引擎会先将重做日志信息放入到缓冲区中，然后再刷新到重做日志文件中。</p>
<h3>2. 后台线程</h3>
<p>Master Thread 主要负责将缓冲池中的数据异步刷新到磁盘中，除此之外还包括插入缓存、undo 页的回收等，IO Thread 是负责读写 IO 的线程，而 Purge Thread 主要用于回收事务已经提交了的 undo log，Pager Cleaner Thread 是新引入的一个用于协助 Master Thread 刷新脏页到磁盘的线程，它可以减轻 Master Thread 的工作压力，减少阻塞。</p>
<h3>3. 存储文件</h3>
<p>在 MySQL 中建立一张表都会生成一个.frm 文件，该文件是用来保存每个表的元数据信息的，主要包含表结构定义。</p>
<p>在 InnoDB 中，存储数据都是按表空间进行存放的，默认为共享表空间，存储的文件即为共享表空间文件（ibdata1）。若设置了参数 innodb_file_per_table 为 1，则会将存储的数据、索引等信息单独存储在一个独占表空间，因此也会产生一个独占表空间文件（ibd）。如果你对共享表空间和独占表空间的理解还不够透彻，接下来我会详解。</p>
<p>而日志文件则主要是重做日志文件，主要记录事务产生的重做日志，保证事务的一致性。</p>
<h2>InnoDB 逻辑存储结构</h2>
<p>InnoDB 逻辑存储结构分为表空间（Tablespace）、段 (Segment)、区 (Extent)、页 Page) 以及行 (row)。</p>
<p><img src="assets/88b4ae3373eb5428c238b70423a13e76.jpg" alt="img" /></p>
<h3>1. 表空间（Tablespace）</h3>
<p>InnoDB 提供了两种表空间存储数据的方式，一种是共享表空间，一种是独占表空间。 InnoDB 默认会将其所有的表数据存储在一个共享表空间中，即 ibdata1。</p>
<p>我们可以通过设置 innodb_file_per_table 参数为 1（1 代表独占方式）开启独占表空间模式。开启之后，每个表都有自己独立的表空间物理文件，所有的数据以及索引都会存储在该文件中，这样方便备份以及恢复数据。</p>
<h3>2. 段 (Segment)</h3>
<p>表空间是由各个段组成的，段一般分为数据段、索引段和回滚段等。我们知道，InnoDB 默认是基于 B + 树实现的数据存储。</p>
<p>这里的索引段则是指的 B + 树的非叶子节点，而数据段则是 B + 树的叶子节点。而回滚段则指的是回滚数据，之前我们在讲事务隔离的时候就介绍到了 MVCC 利用了回滚段实现了多版本查询数据。</p>
<h3>3. 区 (Extent) / 页（Page）</h3>
<p>区是表空间的单元结构，每个区的大小为 1MB。而页是组成区的最小单元，页也是 InnoDB 存储引擎磁盘管理的最小单元，每个页的大小默认为 16KB。为了保证页的连续性，InnoDB 存储引擎每次从磁盘申请 4-5 个区。</p>
<h3>4. 行（Row）</h3>
<p>InnoDB 存储引擎是面向列的（row-oriented)，也就是说数据是按行进行存放的，每个页存放的行记录也是有硬性定义的，最多允许存放 16KB/2-200 行，即 7992 行记录。</p>
<h2>InnoDB 事务之 redo log 工作原理</h2>
<p>InnoDB 是一个事务性的存储引擎，而 InnoDB 的事务实现是基于事务日志 redo log 和 undo log 实现的。redo log 是重做日志，提供再写入操作，实现事务的持久性；undo log 是回滚日志，提供回滚操作，保证事务的一致性。</p>
<p>redo log 又包括了内存中的日志缓冲（redo log buffer）以及保存在磁盘的重做日志文件（redo log file），前者存储在内存中，容易丢失，后者持久化在磁盘中，不会丢失。</p>
<p>InnoDB 的更新操作采用的是 Write Ahead Log 策略，即先写日志，再写入磁盘。当一条记录更新时，InnoDB 会先把记录写入到 redo log buffer 中，并更新内存数据。我们可以通过参数 innodb_flush_log_at_trx_commit 自定义 commit 时，如何将 redo log buffer 中的日志刷新到 redo log file 中。</p>
<p>在这里，我们需要注意的是 InnoDB 的 redo log 的大小是固定的，分别有多个日志文件采用循环方式组成一个循环闭环，当写到结尾时，会回到开头循环写日志。我们可以通过参数 innodb_log_files_in_group 和 innodb_log_file_size 配置日志文件数量和每个日志文件的大小。</p>
<p>Buffer Pool 中更新的数据未刷新到磁盘中，该内存页我们称之为脏页。最终脏页的数据会刷新到磁盘中，将磁盘中的数据覆盖，这个过程与 redo log 不一定有关系。</p>
<p>只有当 redo log 日志满了的情况下，才会主动触发脏页刷新到磁盘，而脏页不仅只有 redo log 日志满了的情况才会刷新到磁盘，以下几种情况同样会触发脏页的刷新：</p>
<ul>
<li>系统内存不足时，需要将一部分数据页淘汰掉，如果淘汰的是脏页，需要先将脏页同步到磁盘；</li>
<li>MySQL 认为空闲的时间，这种情况没有性能问题；</li>
<li>MySQL 正常关闭之前，会把所有的脏页刷入到磁盘，这种情况也没有性能问题。</li>
</ul>
<p>在生产环境中，如果我们开启了慢 SQL 监控，你会发现偶尔会出现一些用时稍长的 SQL。这是因为脏页在刷新到磁盘时可能会给数据库带来性能开销，导致数据库操作抖动。</p>
<p><img src="assets/2a32f1dc2dfbb1f9bc169ee55174d2fd.jpg" alt="img" /></p>
<h2>LRU 淘汰策略</h2>
<p>以上我们了解了 InnoDB 的更新和插入操作的具体实现原理，接下来我们再来了解下读的实现和优化方式。</p>
<p>InnoDB 存储引擎是基于集合索引实现的数据存储，也就是除了索引列以及主键是存储在 B + 树之外，其它列数据也存储在 B + 树的叶子节点中。而这里的索引页和数据页都会缓存在缓冲池中，在查询数据时，只要在缓冲池中存在该数据，InnoDB 就不用每次都去磁盘中读取页，从而提高数据库的查询性能。</p>
<p>虽然缓冲池是一个很大的内存区域，但由于存放了各种类型的数据，加上存储数据量之大，缓冲池无法将所有的数据都存储在其中。因此，缓冲池需要通过 LRU 算法将最近且经常查询的数据缓存在其中，而不常查询的数据就淘汰出去。</p>
<p>InnoDB 对 LRU 做了一些优化，我们熟悉的 LRU 算法通常是将最近查询的数据放到 LRU 列表的首部，而 InnoDB 则是将数据放在一个 midpoint 位置，通常这个 midpoint 为列表长度的 5/8。</p>
<p>这种策略主要是为了避免一些不常查询的操作突然将热点数据淘汰出去，而热点数据被再次查询时，需要再次从磁盘中获取，从而影响数据库的查询性能。</p>
<p>如果我们的热点数据比较多，我们可以通过调整 midpoint 值来增加热点数据的存储量，从而降低热点数据的淘汰率。</p>
<h2>总结</h2>
<p>以上 InnoDB 的实现和运行原理到这里就介绍完了。回顾模块六，前三讲我主要介绍了数据库操作的性能优化，包括 SQL 语句、事务以及索引的优化，接下来我又讲到了数据库表优化，包括表设计、分表分库的实现等等，最后我还介绍了一些数据库参数的调优。</p>
<p>总的来讲，作为开发工程师，我们应该掌握数据库几个大的知识点，然后再深入到数据库内部实现的细节，这样才能避免经常写出一些具有性能问题的 SQL，培养调优数据库性能的能力。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="38&#32;&#32;数据库参数设置优化，失之毫厘差之千里.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="41&#32;&#32;如何设计更优的分布式锁？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43448b6c8070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
