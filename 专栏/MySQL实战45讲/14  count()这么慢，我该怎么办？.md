<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14  count()这么慢，我该怎么办？.md</title>
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

                    <a class="current-tab" href="14&#32;&#32;count()这么慢，我该怎么办？.md">14  count()这么慢，我该怎么办？.md</a>
                    

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

                    
                    <a href="38&#32;&#32;都说InnoDB好，那还要不要使用Memory引擎？.md">38  都说InnoDB好，那还要不要使用Memory引擎？.md</a>

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
                        <div><h1>14  count()这么慢，我该怎么办？</h1>
<p>在开发系统的时候，你可能经常需要计算一个表的行数，比如一个交易系统的所有变更记录总数。这时候你可能会想，一条 select count(*) from t 语句不就解决了吗？</p>
<p>但是，你会发现随着系统中记录数越来越多，这条语句执行得也会越来越慢。然后你可能就想了，MySQL 怎么这么笨啊，记个总数，每次要查的时候直接读出来，不就好了吗。</p>
<p>那么今天，我们就来聊聊 count(*) 语句到底是怎样实现的，以及 MySQL 为什么会这么实现。然后，我会再和你说说，如果应用中有这种频繁变更并需要统计表行数的需求，业务设计上可以怎么做。</p>
<h1>count(*) 的实现方式</h1>
<p>你首先要明确的是，在不同的 MySQL 引擎中，count(*) 有不同的实现方式。</p>
<ul>
<li>MyISAM 引擎把一个表的总行数存在了磁盘上，因此执行 count(*) 的时候会直接返回这个数，效率很高；</li>
<li>而 InnoDB 引擎就麻烦了，它执行 count(*) 的时候，需要把数据一行一行地从引擎里面读出来，然后累积计数。</li>
</ul>
<p>这里需要注意的是，我们在这篇文章里讨论的是没有过滤条件的 count(*)，如果加了 where 条件的话，MyISAM 表也是不能返回得这么快的。</p>
<p>在前面的文章中，我们一起分析了为什么要使用 InnoDB，因为不论是在事务支持、并发能力还是在数据安全方面，InnoDB 都优于 MyISAM。我猜你的表也一定是用了 InnoDB 引擎。这就是当你的记录数越来越多的时候，计算一个表的总行数会越来越慢的原因。</p>
<p>那<strong>为什么 InnoDB 不跟 MyISAM 一样，也把数字存起来呢？</strong></p>
<p>这是因为即使是在同一个时刻的多个查询，由于多版本并发控制（MVCC）的原因，InnoDB 表“应该返回多少行”也是不确定的。这里，我用一个算 count(*) 的例子来为你解释一下。</p>
<p>假设表 t 中现在有 10000 条记录，我们设计了三个用户并行的会话。</p>
<ul>
<li>会话 A 先启动事务并查询一次表的总行数；</li>
<li>会话 B 启动事务，插入一行后记录后，查询表的总行数；</li>
<li>会话 C 先启动一个单独的语句，插入一行记录后，查询表的总行数。</li>
</ul>
<p>我们假设从上到下是按照时间顺序执行的，同一行语句是在同一时刻执行的。</p>
<p><img src="assets/5e716ba1d464c8224c1c1f36135d0e97.png" alt="img" /></p>
<p>图 1 会话 A、B、C 的执行流程</p>
<p>你会看到，在最后一个时刻，三个会话 A、B、C 会同时查询表 t 的总行数，但拿到的结果却不同。</p>
<p>这和 InnoDB 的事务设计有关系，可重复读是它默认的隔离级别，在代码上就是通过多版本并发控制，也就是 MVCC 来实现的。每一行记录都要判断自己是否对这个会话可见，因此对于 count(*) 请求来说，InnoDB 只好把数据一行一行地读出依次判断，可见的行才能够用于计算“基于这个查询”的表的总行数。</p>
<blockquote>
<p>备注：如果你对 MVCC 记忆模糊了，可以再回顾下第 3 篇文章[《事务隔离：为什么你改了我还看不见？》]和第 8 篇文章[《事务到底是隔离的还是不隔离的？》]中的相关内容。</p>
</blockquote>
<p>当然，现在这个看上去笨笨的 MySQL，在执行 count(*) 操作的时候还是做了优化的。</p>
<p>你知道的，InnoDB 是索引组织表，主键索引树的叶子节点是数据，而普通索引树的叶子节点是主键值。所以，普通索引树比主键索引树小很多。对于 count(*) 这样的操作，遍历哪个索引树得到的结果逻辑上都是一样的。因此，MySQL 优化器会找到最小的那棵树来遍历。<strong>在保证逻辑正确的前提下，尽量减少扫描的数据量，是数据库系统设计的通用法则之一。</strong></p>
<p>如果你用过 show table status 命令的话，就会发现这个命令的输出结果里面也有一个 TABLE_ROWS 用于显示这个表当前有多少行，这个命令执行挺快的，那这个 TABLE_ROWS 能代替 count(*) 吗？</p>
<p>你可能还记得在第 10 篇文章[《 MySQL 为什么有时候会选错索引？》]中我提到过，索引统计的值是通过采样来估算的。实际上，TABLE_ROWS 就是从这个采样估算得来的，因此它也很不准。有多不准呢，官方文档说误差可能达到 40% 到 50%。<strong>所以，show table status 命令显示的行数也不能直接使用。</strong></p>
<p>到这里我们小结一下：</p>
<ul>
<li>MyISAM 表虽然 count(*) 很快，但是不支持事务；</li>
<li>show table status 命令虽然返回很快，但是不准确；</li>
<li>InnoDB 表直接 count(*) 会遍历全表，虽然结果准确，但会导致性能问题。</li>
</ul>
<p>那么，回到文章开头的问题，如果你现在有一个页面经常要显示交易系统的操作记录总数，到底应该怎么办呢？答案是，我们只能自己计数。</p>
<p>接下来，我们讨论一下，看看自己计数有哪些方法，以及每种方法的优缺点有哪些。</p>
<p>这里，我先和你说一下这些方法的基本思路：你需要自己找一个地方，把操作记录表的行数存起来。</p>
<h1>用缓存系统保存计数</h1>
<p>对于更新很频繁的库来说，你可能会第一时间想到，用缓存系统来支持。</p>
<p>你可以用一个 Redis 服务来保存这个表的总行数。这个表每被插入一行 Redis 计数就加 1，每被删除一行 Redis 计数就减 1。这种方式下，读和更新操作都很快，但你再想一下这种方式存在什么问题吗？</p>
<p>没错，缓存系统可能会丢失更新。</p>
<p>Redis 的数据不能永久地留在内存里，所以你会找一个地方把这个值定期地持久化存储起来。但即使这样，仍然可能丢失更新。试想如果刚刚在数据表中插入了一行，Redis 中保存的值也加了 1，然后 Redis 异常重启了，重启后你要从存储 redis 数据的地方把这个值读回来，而刚刚加 1 的这个计数操作却丢失了。</p>
<p>当然了，这还是有解的。比如，Redis 异常重启以后，到数据库里面单独执行一次 count(*) 获取真实的行数，再把这个值写回到 Redis 里就可以了。异常重启毕竟不是经常出现的情况，这一次全表扫描的成本，还是可以接受的。</p>
<p>但实际上，<strong>将计数保存在缓存系统中的方式，还不只是丢失更新的问题。即使 Redis 正常工作，这个值还是逻辑上不精确的。</strong></p>
<p>你可以设想一下有这么一个页面，要显示操作记录的总数，同时还要显示最近操作的 100 条记录。那么，这个页面的逻辑就需要先到 Redis 里面取出计数，再到数据表里面取数据记录。</p>
<p>我们是这么定义不精确的：</p>
<ol>
<li>一种是，查到的 100 行结果里面有最新插入记录，而 Redis 的计数里还没加 1；</li>
<li>另一种是，查到的 100 行结果里没有最新插入的记录，而 Redis 的计数里已经加了 1。</li>
</ol>
<p>这两种情况，都是逻辑不一致的。</p>
<p>我们一起来看看这个时序图。</p>
<p><img src="assets/39898af053695dad37227d71ae288e33.png" alt="img" /></p>
<p>图 2 会话 A、B 执行时序图</p>
<p>图 2 中，会话 A 是一个插入交易记录的逻辑，往数据表里插入一行 R，然后 Redis 计数加 1；会话 B 就是查询页面显示时需要的数据。</p>
<p>在图 2 的这个时序里，在 T3 时刻会话 B 来查询的时候，会显示出新插入的 R 这个记录，但是 Redis 的计数还没加 1。这时候，就会出现我们说的数据不一致。</p>
<p>你一定会说，这是因为我们执行新增记录逻辑时候，是先写数据表，再改 Redis 计数。而读的时候是先读 Redis，再读数据表，这个顺序是相反的。那么，如果保持顺序一样的话，是不是就没问题了？我们现在把会话 A 的更新顺序换一下，再看看执行结果。</p>
<p><img src="assets/5c2f786beae1d8917cdc5033b7bf0bdb.png" alt="img" /></p>
<p>图 3 调整顺序后，会话 A、B 的执行时序图</p>
<p>你会发现，这时候反过来了，会话 B 在 T3 时刻查询的时候，Redis 计数加了 1 了，但还查不到新插入的 R 这一行，也是数据不一致的情况。</p>
<p>在并发系统里面，我们是无法精确控制不同线程的执行时刻的，因为存在图中的这种操作序列，所以，我们说即使 Redis 正常工作，这个计数值还是逻辑上不精确的。</p>
<h1>在数据库保存计数</h1>
<p>根据上面的分析，用缓存系统保存计数有丢失数据和计数不精确的问题。那么，<strong>如果我们把这个计数直接放到数据库里单独的一张计数表 C 中，又会怎么样呢？</strong></p>
<p>首先，这解决了崩溃丢失的问题，InnoDB 是支持崩溃恢复不丢数据的。</p>
<blockquote>
<p>备注：关于 InnoDB 的崩溃恢复，你可以再回顾一下第 2 篇文章[《日志系统：一条 SQL 更新语句是如何执行的？》]中的相关内容。</p>
</blockquote>
<p>然后，我们再看看能不能解决计数不精确的问题。</p>
<p>你会说，这不一样吗？无非就是把图 3 中对 Redis 的操作，改成了对计数表 C 的操作。只要出现图 3 的这种执行序列，这个问题还是无解的吧？</p>
<p>这个问题还真不是无解的。</p>
<p>我们这篇文章要解决的问题，都是由于 InnoDB 要支持事务，从而导致 InnoDB 表不能把 count(*) 直接存起来，然后查询的时候直接返回形成的。</p>
<p>所谓以子之矛攻子之盾，现在我们就利用“事务”这个特性，把问题解决掉。</p>
<p><img src="assets/9e4170e2dfca3524eb5e92adb8647de3.png" alt="img" /></p>
<p>图 4 会话 A、B 的执行时序图</p>
<p>我们来看下现在的执行结果。虽然会话 B 的读操作仍然是在 T3 执行的，但是因为这时候更新事务还没有提交，所以计数值加 1 这个操作对会话 B 还不可见。</p>
<p>因此，会话 B 看到的结果里， 查计数值和“最近 100 条记录”看到的结果，逻辑上就是一致的。</p>
<h1>不同的 count 用法</h1>
<p>在前面文章的评论区，有同学留言问到：在 select count(?) from t 这样的查询语句里面，count(<em>)、count(主键 id)、count(字段) 和 count(1) 等不同用法的性能，有哪些差别。今天谈到了 count(</em>) 的性能问题，我就借此机会和你详细说明一下这几种用法的性能差别。</p>
<p>需要注意的是，下面的讨论还是基于 InnoDB 引擎的。</p>
<p>这里，首先你要弄清楚 count() 的语义。count() 是一个聚合函数，对于返回的结果集，一行行地判断，如果 count 函数的参数不是 NULL，累计值就加 1，否则不加。最后返回累计值。</p>
<p>所以，count(*)、count(主键 id) 和 count(1) 都表示返回满足条件的结果集的总行数；而 count(字段），则表示返回满足条件的数据行里面，参数“字段”不为 NULL 的总个数。</p>
<p>至于分析性能差别的时候，你可以记住这么几个原则：</p>
<ol>
<li>server 层要什么就给什么；</li>
<li>InnoDB 只给必要的值；</li>
<li>现在的优化器只优化了 count(*) 的语义为“取行数”，其他“显而易见”的优化并没有做。</li>
</ol>
<p>这是什么意思呢？接下来，我们就一个个地来看看。</p>
<p><strong>对于 count(主键 id) 来说</strong>，InnoDB 引擎会遍历整张表，把每一行的 id 值都取出来，返回给 server 层。server 层拿到 id 后，判断是不可能为空的，就按行累加。</p>
<p><strong>对于 count(1) 来说</strong>，InnoDB 引擎遍历整张表，但不取值。server 层对于返回的每一行，放一个数字“1”进去，判断是不可能为空的，按行累加。</p>
<p>单看这两个用法的差别的话，你能对比出来，count(1) 执行得要比 count(主键 id) 快。因为从引擎返回 id 会涉及到解析数据行，以及拷贝字段值的操作。</p>
<p><strong>对于 count(字段) 来说</strong>：</p>
<ol>
<li>如果这个“字段”是定义为 not null 的话，一行行地从记录里面读出这个字段，判断不能为 null，按行累加；</li>
<li>如果这个“字段”定义允许为 null，那么执行的时候，判断到有可能是 null，还要把值取出来再判断一下，不是 null 才累加。</li>
</ol>
<p>也就是前面的第一条原则，server 层要什么字段，InnoDB 就返回什么字段。</p>
<p><strong>但是 count(*) 是例外</strong>，并不会把全部字段取出来，而是专门做了优化，不取值。count(*) 肯定不是 null，按行累加。</p>
<p>看到这里，你一定会说，优化器就不能自己判断一下吗，主键 id 肯定非空啊，为什么不能按照 count(*) 来处理，多么简单的优化啊。</p>
<p>当然，MySQL 专门针对这个语句进行优化，也不是不可以。但是这种需要专门优化的情况太多了，而且 MySQL 已经优化过 count(*) 了，你直接使用这种用法就可以了。</p>
<p>所以结论是：按照效率排序的话，count(字段)&lt;count(主键 id)&lt;count(1)≈count(<em>)，所以我建议你，尽量使用 count(</em>)。</p>
<h1>小结</h1>
<p>今天，我和你聊了聊 MySQL 中获得表行数的两种方法。我们提到了在不同引擎中 count(*) 的实现方式是不一样的，也分析了用缓存系统来存储计数值存在的问题。</p>
<p>其实，把计数放在 Redis 里面，不能够保证计数和 MySQL 表里的数据精确一致的原因，是**这两个不同的存储构成的系统，不支持分布式事务，无法拿到精确一致的视图。**而把计数值也放在 MySQL 中，就解决了一致性视图的问题。</p>
<p>InnoDB 引擎支持事务，我们利用好事务的原子性和隔离性，就可以简化在业务开发时的逻辑。这也是 InnoDB 引擎备受青睐的原因之一。</p>
<p>最后，又到了今天的思考题时间了。</p>
<p>在刚刚讨论的方案中，我们用了事务来确保计数准确。由于事务可以保证中间结果不被别的事务读到，因此修改计数值和插入新记录的顺序是不影响逻辑结果的。但是，从并发系统性能的角度考虑，你觉得在这个事务序列里，应该先插入操作记录，还是应该先更新计数表呢？</p>
<p>你可以把你的思考和观点写在留言区里，我会在下一篇文章的末尾给出我的参考答案。感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。</p>
<h1>上期问题时间</h1>
<p>上期我给你留的问题是，什么时候使用 alter table t engine=InnoDB 会让一个表占用的空间反而变大。</p>
<p>在这篇文章的评论区里面，大家都提到了一个点，就是这个表，本身就已经没有空洞的了，比如说刚刚做过一次重建表操作。</p>
<p>在 DDL 期间，如果刚好有外部的 DML 在执行，这期间可能会引入一些新的空洞。</p>
<p>@飞翔 提到了一个更深刻的机制，是我们在文章中没说的。在重建表的时候，InnoDB 不会把整张表占满，每个页留了 1/16 给后续的更新用。也就是说，其实重建表之后不是“最”紧凑的。</p>
<p>假如是这么一个过程：</p>
<ol>
<li>将表 t 重建一次；</li>
<li>插入一部分数据，但是插入的这些数据，用掉了一部分的预留空间；</li>
<li>这种情况下，再重建一次表 t，就可能会出现问题中的现象。</li>
</ol>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;&#32;为什么表数据删掉一半，表文件大小不变？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;&#32;答疑文章（一）：日志和索引相关问题.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43471be98970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
