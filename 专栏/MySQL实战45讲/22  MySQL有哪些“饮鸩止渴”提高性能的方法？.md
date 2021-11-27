<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>22  MySQL有哪些“饮鸩止渴”提高性能的方法？.md</title>
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

                    <a class="current-tab" href="22&#32;&#32;MySQL有哪些“饮鸩止渴”提高性能的方法？.md">22  MySQL有哪些“饮鸩止渴”提高性能的方法？.md</a>
                    

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
                        <div><h1>22  MySQL有哪些“饮鸩止渴”提高性能的方法？</h1>
<p>不知道你在实际运维过程中有没有碰到这样的情景：业务高峰期，生产环境的 MySQL 压力太大，没法正常响应，需要短期内、临时性地提升一些性能。</p>
<p>我以前做业务护航的时候，就偶尔会碰上这种场景。用户的开发负责人说，不管你用什么方案，让业务先跑起来再说。</p>
<p>但，如果是无损方案的话，肯定不需要等到这个时候才上场。今天我们就来聊聊这些临时方案，并着重说一说它们可能存在的风险。</p>
<h1>短连接风暴</h1>
<p>正常的短连接模式就是连接到数据库后，执行很少的 SQL 语句就断开，下次需要的时候再重连。如果使用的是短连接，在业务高峰期的时候，就可能出现连接数突然暴涨的情况。</p>
<p>我在第 1 篇文章[《基础架构：一条 SQL 查询语句是如何执行的？》]中说过，MySQL 建立连接的过程，成本是很高的。除了正常的网络连接三次握手外，还需要做登录权限判断和获得这个连接的数据读写权限。</p>
<p>在数据库压力比较小的时候，这些额外的成本并不明显。</p>
<p>但是，短连接模型存在一个风险，就是一旦数据库处理得慢一些，连接数就会暴涨。max_connections 参数，用来控制一个 MySQL 实例同时存在的连接数的上限，超过这个值，系统就会拒绝接下来的连接请求，并报错提示“Too many connections”。对于被拒绝连接的请求来说，从业务角度看就是数据库不可用。</p>
<p>在机器负载比较高的时候，处理现有请求的时间变长，每个连接保持的时间也更长。这时，再有新建连接的话，就可能会超过 max_connections 的限制。</p>
<p>碰到这种情况时，一个比较自然的想法，就是调高 max_connections 的值。但这样做是有风险的。因为设计 max_connections 这个参数的目的是想保护 MySQL，如果我们把它改得太大，让更多的连接都可以进来，那么系统的负载可能会进一步加大，大量的资源耗费在权限验证等逻辑上，结果可能是适得其反，已经连接的线程拿不到 CPU 资源去执行业务的 SQL 请求。</p>
<p>那么这种情况下，你还有没有别的建议呢？我这里还有两种方法，但要注意，这些方法都是有损的。</p>
<p><strong>第一种方法：先处理掉那些占着连接但是不工作的线程。</strong></p>
<p>max_connections 的计算，不是看谁在 running，是只要连着就占用一个计数位置。对于那些不需要保持的连接，我们可以通过 kill connection 主动踢掉。这个行为跟事先设置 wait_timeout 的效果是一样的。设置 wait_timeout 参数表示的是，一个线程空闲 wait_timeout 这么多秒之后，就会被 MySQL 直接断开连接。</p>
<p>但是需要注意，在 show processlist 的结果里，踢掉显示为 sleep 的线程，可能是有损的。我们来看下面这个例子。</p>
<p><img src="assets/9091ff280592c8c68665771b1516c62a.png" alt="img" /></p>
<p>图 1 sleep 线程的两种状态</p>
<p>在上面这个例子里，如果断开 session A 的连接，因为这时候 session A 还没有提交，所以 MySQL 只能按照回滚事务来处理；而断开 session B 的连接，就没什么大影响。所以，如果按照优先级来说，你应该优先断开像 session B 这样的事务外空闲的连接。</p>
<p>但是，怎么判断哪些是事务外空闲的呢？session C 在 T 时刻之后的 30 秒执行 show processlist，看到的结果是这样的。</p>
<p><img src="assets/ae6a9ceecf8517e47f9ebfc565f0f925.png" alt="img" /></p>
<p>图 2 sleep 线程的两种状态，show processlist 结果</p>
<p>图中 id=4 和 id=5 的两个会话都是 Sleep 状态。而要看事务具体状态的话，你可以查 information_schema 库的 innodb_trx 表。</p>
<p><img src="assets/ca4b455c8eacbf32b98d1fe9ed9876e8.png" alt="img" /></p>
<p>图 3 从 information_schema.innodb_trx 查询事务状态</p>
<p>这个结果里，trx_mysql_thread_id=4，表示 id=4 的线程还处在事务中。</p>
<p>因此，如果是连接数过多，你可以优先断开事务外空闲太久的连接；如果这样还不够，再考虑断开事务内空闲太久的连接。</p>
<p>从服务端断开连接使用的是 kill connection + id 的命令， 一个客户端处于 sleep 状态时，它的连接被服务端主动断开后，这个客户端并不会马上知道。直到客户端在发起下一个请求的时候，才会收到这样的报错“ERROR 2013 (HY000): Lost connection to MySQL server during query”。</p>
<p>从数据库端主动断开连接可能是有损的，尤其是有的应用端收到这个错误后，不重新连接，而是直接用这个已经不能用的句柄重试查询。这会导致从应用端看上去，“MySQL 一直没恢复”。</p>
<p>你可能觉得这是一个冷笑话，但实际上我碰到过不下 10 次。</p>
<p>所以，如果你是一个支持业务的 DBA，不要假设所有的应用代码都会被正确地处理。即使只是一个断开连接的操作，也要确保通知到业务开发团队。</p>
<p><strong>第二种方法：减少连接过程的消耗。</strong></p>
<p>有的业务代码会在短时间内先大量申请数据库连接做备用，如果现在数据库确认是被连接行为打挂了，那么一种可能的做法，是让数据库跳过权限验证阶段。</p>
<p>跳过权限验证的方法是：重启数据库，并使用–skip-grant-tables 参数启动。这样，整个 MySQL 会跳过所有的权限验证阶段，包括连接过程和语句执行过程在内。</p>
<p>但是，这种方法特别符合我们标题里说的“饮鸩止渴”，风险极高，是我特别不建议使用的方案。尤其你的库外网可访问的话，就更不能这么做了。</p>
<p>在 MySQL 8.0 版本里，如果你启用–skip-grant-tables 参数，MySQL 会默认把 --skip-networking 参数打开，表示这时候数据库只能被本地的客户端连接。可见，MySQL 官方对 skip-grant-tables 这个参数的安全问题也很重视。</p>
<p>除了短连接数暴增可能会带来性能问题外，实际上，我们在线上碰到更多的是查询或者更新语句导致的性能问题。其中，查询问题比较典型的有两类，一类是由新出现的慢查询导致的，一类是由 QPS（每秒查询数）突增导致的。而关于更新语句导致的性能问题，我会在下一篇文章和你展开说明。</p>
<h1>慢查询性能问题</h1>
<p>在 MySQL 中，会引发性能问题的慢查询，大体有以下三种可能：</p>
<ol>
<li>索引没有设计好；</li>
<li>SQL 语句没写好；</li>
<li>MySQL 选错了索引。</li>
</ol>
<p>接下来，我们就具体分析一下这三种可能，以及对应的解决方案。</p>
<p><strong>导致慢查询的第一种可能是，索引没有设计好。</strong></p>
<p>这种场景一般就是通过紧急创建索引来解决。MySQL 5.6 版本以后，创建索引都支持 Online DDL 了，对于那种高峰期数据库已经被这个语句打挂了的情况，最高效的做法就是直接执行 alter table 语句。</p>
<p>比较理想的是能够在备库先执行。假设你现在的服务是一主一备，主库 A、备库 B，这个方案的大致流程是这样的：</p>
<ol>
<li>在备库 B 上执行 set sql_log_bin=off，也就是不写 binlog，然后执行 alter table 语句加上索引；</li>
<li>执行主备切换；</li>
<li>这时候主库是 B，备库是 A。在 A 上执行 set sql_log_bin=off，然后执行 alter table 语句加上索引。</li>
</ol>
<p>这是一个“古老”的 DDL 方案。平时在做变更的时候，你应该考虑类似 gh-ost 这样的方案，更加稳妥。但是在需要紧急处理时，上面这个方案的效率是最高的。</p>
<p><strong>导致慢查询的第二种可能是，语句没写好。</strong></p>
<p>比如，我们犯了在第 18 篇文章[《为什么这些 SQL 语句逻辑相同，性能却差异巨大？》]中提到的那些错误，导致语句没有使用上索引。</p>
<p>这时，我们可以通过改写 SQL 语句来处理。MySQL 5.7 提供了 query_rewrite 功能，可以把输入的一种语句改写成另外一种模式。</p>
<p>比如，语句被错误地写成了 select * from t where id + 1 = 10000，你可以通过下面的方式，增加一个语句改写规则。</p>
<pre><code>mysql&gt; insert into query_rewrite.rewrite_rules(pattern, replacement, pattern_database) values (&quot;select * from t where id + 1 = ?&quot;, &quot;select * from t where id = ? - 1&quot;, &quot;db1&quot;);
 
call query_rewrite.flush_rewrite_rules();
</code></pre>
<p>这里，call query_rewrite.flush_rewrite_rules() 这个存储过程，是让插入的新规则生效，也就是我们说的“查询重写”。你可以用图 4 中的方法来确认改写规则是否生效。</p>
<p><img src="assets/47a1002cbc4c05c74841591d20f7388a.png" alt="img" /></p>
<p>图 4 查询重写效果</p>
<p><strong>导致慢查询的第三种可能，就是碰上了我们在第 10 篇文章</strong>[<strong>《MySQL 为什么有时候会选错索引？》</strong>]<strong>中提到的情况，MySQL 选错了索引。</strong></p>
<p>这时候，应急方案就是给这个语句加上 force index。</p>
<p>同样地，使用查询重写功能，给原来的语句加上 force index，也可以解决这个问题。</p>
<p>上面我和你讨论的由慢查询导致性能问题的三种可能情况，实际上出现最多的是前两种，即：索引没设计好和语句没写好。而这两种情况，恰恰是完全可以避免的。比如，通过下面这个过程，我们就可以预先发现问题。</p>
<ol>
<li>上线前，在测试环境，把慢查询日志（slow log）打开，并且把 long_query_time 设置成 0，确保每个语句都会被记录入慢查询日志；</li>
<li>在测试表里插入模拟线上的数据，做一遍回归测试；</li>
<li>观察慢查询日志里每类语句的输出，特别留意 Rows_examined 字段是否与预期一致。（我们在前面文章中已经多次用到过 Rows_examined 方法了，相信你已经动手尝试过了。如果还有不明白的，欢迎给我留言，我们一起讨论）。</li>
</ol>
<p>不要吝啬这段花在上线前的“额外”时间，因为这会帮你省下很多故障复盘的时间。</p>
<p>如果新增的 SQL 语句不多，手动跑一下就可以。而如果是新项目的话，或者是修改了原有项目的 表结构设计，全量回归测试都是必要的。这时候，你需要工具帮你检查所有的 SQL 语句的返回结果。比如，你可以使用开源工具 pt-query-digest(<a href="https://www.percona.com/doc/percona-toolkit/3.0/pt-query-digest.html">https://www.percona.com/doc/percona-toolkit/3.0/pt-query-digest.html</a>)。</p>
<h1>QPS 突增问题</h1>
<p>有时候由于业务突然出现高峰，或者应用程序 bug，导致某个语句的 QPS 突然暴涨，也可能导致 MySQL 压力过大，影响服务。</p>
<p>我之前碰到过一类情况，是由一个新功能的 bug 导致的。当然，最理想的情况是让业务把这个功能下掉，服务自然就会恢复。</p>
<p>而下掉一个功能，如果从数据库端处理的话，对应于不同的背景，有不同的方法可用。我这里再和你展开说明一下。</p>
<ol>
<li>一种是由全新业务的 bug 导致的。假设你的 DB 运维是比较规范的，也就是说白名单是一个个加的。这种情况下，如果你能够确定业务方会下掉这个功能，只是时间上没那么快，那么就可以从数据库端直接把白名单去掉。</li>
<li>如果这个新功能使用的是单独的数据库用户，可以用管理员账号把这个用户删掉，然后断开现有连接。这样，这个新功能的连接不成功，由它引发的 QPS 就会变成 0。</li>
<li>如果这个新增的功能跟主体功能是部署在一起的，那么我们只能通过处理语句来限制。这时，我们可以使用上面提到的查询重写功能，把压力最大的 SQL 语句直接重写成&quot;select 1&quot;返回。</li>
</ol>
<p>当然，这个操作的风险很高，需要你特别细致。它可能存在两个副作用：</p>
<ol>
<li>如果别的功能里面也用到了这个 SQL 语句模板，会有误伤；</li>
<li>很多业务并不是靠这一个语句就能完成逻辑的，所以如果单独把这一个语句以 select 1 的结果返回的话，可能会导致后面的业务逻辑一起失败。</li>
</ol>
<p>所以，方案 3 是用于止血的，跟前面提到的去掉权限验证一样，应该是你所有选项里优先级最低的一个方案。</p>
<p>同时你会发现，其实方案 1 和 2 都要依赖于规范的运维体系：虚拟化、白名单机制、业务账号分离。由此可见，更多的准备，往往意味着更稳定的系统。</p>
<h1>小结</h1>
<p>今天这篇文章，我以业务高峰期的性能问题为背景，和你介绍了一些紧急处理的手段。</p>
<p>这些处理手段中，既包括了粗暴地拒绝连接和断开连接，也有通过重写语句来绕过一些坑的方法；既有临时的高危方案，也有未雨绸缪的、相对安全的预案。</p>
<p>在实际开发中，我们也要尽量避免一些低效的方法，比如避免大量地使用短连接。同时，如果你做业务开发的话，要知道，连接异常断开是常有的事，你的代码里要有正确地重连并重试的机制。</p>
<p>DBA 虽然可以通过语句重写来暂时处理问题，但是这本身是一个风险高的操作，做好 SQL 审计可以减少需要这类操作的机会。</p>
<p>其实，你可以看得出来，在这篇文章中我提到的解决方法主要集中在 server 层。在下一篇文章中，我会继续和你讨论一些跟 InnoDB 有关的处理方法。</p>
<p>最后，又到了我们的思考题时间了。</p>
<p>今天，我留给你的课后问题是，你是否碰到过，在业务高峰期需要临时救火的场景？你又是怎么处理的呢？</p>
<p>你可以把你的经历和经验写在留言区，我会在下一篇文章的末尾选取有趣的评论跟大家一起分享和分析。感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。</p>
<h1>上期问题时间</h1>
<p>前两期我给你留的问题是，下面这个图的执行序列中，为什么 session B 的 insert 语句会被堵住。</p>
<p><img src="assets/3a7578e104612a188a2d574eaa3bd81e.png" alt="img" />
我们用上一篇的加锁规则来分析一下，看看 session A 的 select 语句加了哪些锁：</p>
<ol>
<li>由于是 order by c desc，第一个要定位的是索引 c 上“最右边的”c=20 的行，所以会加上间隙锁 (20,25) 和 next-key lock (15,20]。</li>
<li>在索引 c 上向左遍历，要扫描到 c=10 才停下来，所以 next-key lock 会加到 (5,10]，这正是阻塞 session B 的 insert 语句的原因。</li>
<li>在扫描过程中，c=20、c=15、c=10 这三行都存在值，由于是 select *，所以会在主键 id 上加三个行锁。</li>
</ol>
<p>因此，session A 的 select 语句锁的范围就是：</p>
<ol>
<li>索引 c 上 (5, 25)；</li>
<li>主键索引上 id=15、20 两个行锁。</li>
</ol>
<p>这里，我再啰嗦下，你会发现我在文章中，每次加锁都会说明是加在“哪个索引上”的。因为，锁就是加在索引上的，这是 InnoDB 的一个基础设定，需要你在分析问题的时候要一直记得。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="21&#32;&#32;为什么我只改一行的语句，锁这么多？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="23&#32;&#32;MySQL是怎么保证数据不丢的？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43474c0eb970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
