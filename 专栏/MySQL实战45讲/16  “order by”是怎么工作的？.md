<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  “order by”是怎么工作的？.md</title>
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

                    <a class="current-tab" href="16&#32;&#32;“order&#32;by”是怎么工作的？.md">16  “order by”是怎么工作的？.md</a>
                    

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
                        <div><h1>16  “order by”是怎么工作的？</h1>
<p>在你开发应用的时候，一定会经常碰到需要根据指定的字段排序来显示结果的需求。还是以我们前面举例用过的市民表为例，假设你要查询城市是“杭州”的所有人名字，并且按照姓名排序返回前 1000 个人的姓名、年龄。</p>
<p>假设这个表的部分定义是这样的：</p>
<pre><code>CREATE TABLE `t` (
  `id` int(11) NOT NULL,
  `city` varchar(16) NOT NULL,
  `name` varchar(16) NOT NULL,
  `age` int(11) NOT NULL,
  `addr` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `city` (`city`)
) ENGINE=InnoDB;
</code></pre>
<p>这时，你的 SQL 语句可以这么写：</p>
<pre><code>select city,name,age from t where city='杭州' order by name limit 1000  ;
</code></pre>
<p>这个语句看上去逻辑很清晰，但是你了解它的执行流程吗？今天，我就和你聊聊这个语句是怎么执行的，以及有什么参数会影响执行的行为。</p>
<h1>全字段排序</h1>
<p>前面我们介绍过索引，所以你现在就很清楚了，为避免全表扫描，我们需要在 city 字段加上索引。</p>
<p>在 city 字段上创建索引之后，我们用 explain 命令来看看这个语句的执行情况。</p>
<p><img src="assets/826579b63225def812330ef6c344a303.png" alt="img" /></p>
<p>图 1 使用 explain 命令查看语句的执行情况</p>
<p>Extra 这个字段中的“Using filesort”表示的就是需要排序，MySQL 会给每个线程分配一块内存用于排序，称为 sort_buffer。</p>
<p>为了说明这个 SQL 查询语句的执行过程，我们先来看一下 city 这个索引的示意图。</p>
<p><img src="assets/5334cca9118be14bde95ec94b02f0a3e.png" alt="img" /></p>
<p>图 2 city 字段的索引示意图</p>
<p>从图中可以看到，满足 city='杭州’条件的行，是从 ID_X 到 ID_(X+N) 的这些记录。</p>
<p>通常情况下，这个语句执行流程如下所示 ：</p>
<ol>
<li>初始化 sort_buffer，确定放入 name、city、age 这三个字段；</li>
<li>从索引 city 找到第一个满足 city='杭州’条件的主键 id，也就是图中的 ID_X；</li>
<li>到主键 id 索引取出整行，取 name、city、age 三个字段的值，存入 sort_buffer 中；</li>
<li>从索引 city 取下一个记录的主键 id；</li>
<li>重复步骤 3、4 直到 city 的值不满足查询条件为止，对应的主键 id 也就是图中的 ID_Y；</li>
<li>对 sort_buffer 中的数据按照字段 name 做快速排序；</li>
<li>按照排序结果取前 1000 行返回给客户端。</li>
</ol>
<p>我们暂且把这个排序过程，称为全字段排序，执行流程的示意图如下所示，下一篇文章中我们还会用到这个排序。</p>
<p><img src="assets/6c821828cddf46670f9d56e126e3e772.jpg" alt="img" /></p>
<p>图 3 全字段排序</p>
<p>图中“按 name 排序”这个动作，可能在内存中完成，也可能需要使用外部排序，这取决于排序所需的内存和参数 sort_buffer_size。</p>
<p>sort_buffer_size，就是 MySQL 为排序开辟的内存（sort_buffer）的大小。如果要排序的数据量小于 sort_buffer_size，排序就在内存中完成。但如果排序数据量太大，内存放不下，则不得不利用磁盘临时文件辅助排序。</p>
<p>你可以用下面介绍的方法，来确定一个排序语句是否使用了临时文件。</p>
<pre><code>/* 打开 optimizer_trace，只对本线程有效 */
SET optimizer_trace='enabled=on'; 
 
/* @a 保存 Innodb_rows_read 的初始值 */
select VARIABLE_VALUE into @a from  performance_schema.session_status where variable_name = 'Innodb_rows_read';
 
/* 执行语句 */
select city, name,age from t where city='杭州' order by name limit 1000; 
 
/* 查看 OPTIMIZER_TRACE 输出 */
SELECT * FROM `information_schema`.`OPTIMIZER_TRACE`\G
 
/* @b 保存 Innodb_rows_read 的当前值 */
select VARIABLE_VALUE into @b from performance_schema.session_status where variable_name = 'Innodb_rows_read';
 
/* 计算 Innodb_rows_read 差值 */
select @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ef8dc2af8e">[email&#160;protected]</a>;
</code></pre>
<p>这个方法是通过查看 OPTIMIZER_TRACE 的结果来确认的，你可以从 number_of_tmp_files 中看到是否使用了临时文件。</p>
<p><img src="assets/89baf99cdeefe90a22370e1d6f5e6495.png" alt="img" /></p>
<p>图 4 全排序的 OPTIMIZER_TRACE 部分结果</p>
<p>number_of_tmp_files 表示的是，排序过程中使用的临时文件数。你一定奇怪，为什么需要 12 个文件？内存放不下时，就需要使用外部排序，外部排序一般使用归并排序算法。可以这么简单理解，<strong>MySQL 将需要排序的数据分成 12 份，每一份单独排序后存在这些临时文件中。然后把这 12 个有序文件再合并成一个有序的大文件。</strong></p>
<p>如果 sort_buffer_size 超过了需要排序的数据量的大小，number_of_tmp_files 就是 0，表示排序可以直接在内存中完成。</p>
<p>否则就需要放在临时文件中排序。sort_buffer_size 越小，需要分成的份数越多，number_of_tmp_files 的值就越大。</p>
<p>接下来，我再和你解释一下图 4 中其他两个值的意思。</p>
<p>我们的示例表中有 4000 条满足 city='杭州’的记录，所以你可以看到 examined_rows=4000，表示参与排序的行数是 4000 行。</p>
<p>sort_mode 里面的 packed_additional_fields 的意思是，排序过程对字符串做了“紧凑”处理。即使 name 字段的定义是 varchar(16)，在排序过程中还是要按照实际长度来分配空间的。</p>
<p>同时，最后一个查询语句 select @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="61034c2100">[email&#160;protected]</a> 的返回结果是 4000，表示整个执行过程只扫描了 4000 行。</p>
<p>这里需要注意的是，为了避免对结论造成干扰，我把 internal_tmp_disk_storage_engine 设置成 MyISAM。否则，select @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ec8ec1ac8d">[email&#160;protected]</a> 的结果会显示为 4001。</p>
<p>这是因为查询 OPTIMIZER_TRACE 这个表时，需要用到临时表，而 internal_tmp_disk_storage_engine 的默认值是 InnoDB。如果使用的是 InnoDB 引擎的话，把数据从临时表取出来的时候，会让 Innodb_rows_read 的值加 1。</p>
<h1>rowid 排序</h1>
<p>在上面这个算法过程里面，只对原表的数据读了一遍，剩下的操作都是在 sort_buffer 和临时文件中执行的。但这个算法有一个问题，就是如果查询要返回的字段很多的话，那么 sort_buffer 里面要放的字段数太多，这样内存里能够同时放下的行数很少，要分成很多个临时文件，排序的性能会很差。</p>
<p>所以如果单行很大，这个方法效率不够好。</p>
<p>那么，<strong>如果 MySQL 认为排序的单行长度太大会怎么做呢？</strong></p>
<p>接下来，我来修改一个参数，让 MySQL 采用另外一种算法。</p>
<pre><code>SET max_length_for_sort_data = 16;
</code></pre>
<p>max_length_for_sort_data，是 MySQL 中专门控制用于排序的行数据的长度的一个参数。它的意思是，如果单行的长度超过这个值，MySQL 就认为单行太大，要换一个算法。</p>
<p>city、name、age 这三个字段的定义总长度是 36，我把 max_length_for_sort_data 设置为 16，我们再来看看计算过程有什么改变。</p>
<p>新的算法放入 sort_buffer 的字段，只有要排序的列（即 name 字段）和主键 id。</p>
<p>但这时，排序的结果就因为少了 city 和 age 字段的值，不能直接返回了，整个执行流程就变成如下所示的样子：</p>
<ol>
<li>初始化 sort_buffer，确定放入两个字段，即 name 和 id；</li>
<li>从索引 city 找到第一个满足 city='杭州’条件的主键 id，也就是图中的 ID_X；</li>
<li>到主键 id 索引取出整行，取 name、id 这两个字段，存入 sort_buffer 中；</li>
<li>从索引 city 取下一个记录的主键 id；</li>
<li>重复步骤 3、4 直到不满足 city='杭州’条件为止，也就是图中的 ID_Y；</li>
<li>对 sort_buffer 中的数据按照字段 name 进行排序；</li>
<li>遍历排序结果，取前 1000 行，并按照 id 的值回到原表中取出 city、name 和 age 三个字段返回给客户端。</li>
</ol>
<p>这个执行流程的示意图如下，我把它称为 rowid 排序。</p>
<p><img src="assets/dc92b67721171206a302eb679c83e86d.jpg" alt="img" /></p>
<p>图 5 rowid 排序</p>
<p>对比图 3 的全字段排序流程图你会发现，rowid 排序多访问了一次表 t 的主键索引，就是步骤 7。</p>
<p>需要说明的是，最后的“结果集”是一个逻辑概念，实际上 MySQL 服务端从排序后的 sort_buffer 中依次取出 id，然后到原表查到 city、name 和 age 这三个字段的结果，不需要在服务端再耗费内存存储结果，是直接返回给客户端的。</p>
<p>根据这个说明过程和图示，你可以想一下，这个时候执行 select @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="97f5bad7f6">[email&#160;protected]</a>，结果会是多少呢？</p>
<p>现在，我们就来看看结果有什么不同。</p>
<p>首先，图中的 examined_rows 的值还是 4000，表示用于排序的数据是 4000 行。但是 select @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d5b7f895b4">[email&#160;protected]</a> 这个语句的值变成 5000 了。</p>
<p>因为这时候除了排序过程外，在排序完成后，还要根据 id 去原表取值。由于语句是 limit 1000，因此会多读 1000 行。</p>
<p><img src="assets/27f164804d1a4689718291be5d10f89b.png" alt="img" /></p>
<p>图 6 rowid 排序的 OPTIMIZER_TRACE 部分输出</p>
<p>从 OPTIMIZER_TRACE 的结果中，你还能看到另外两个信息也变了。</p>
<ul>
<li>sort_mode 变成了 &lt;sort_key, rowid&gt;，表示参与排序的只有 name 和 id 这两个字段。</li>
<li>number_of_tmp_files 变成 10 了，是因为这时候参与排序的行数虽然仍然是 4000 行，但是每一行都变小了，因此需要排序的总数据量就变小了，需要的临时文件也相应地变少了。</li>
</ul>
<h1>全字段排序 VS rowid 排序</h1>
<p>我们来分析一下，从这两个执行流程里，还能得出什么结论。</p>
<p>如果 MySQL 实在是担心排序内存太小，会影响排序效率，才会采用 rowid 排序算法，这样排序过程中一次可以排序更多行，但是需要再回到原表去取数据。</p>
<p>如果 MySQL 认为内存足够大，会优先选择全字段排序，把需要的字段都放到 sort_buffer 中，这样排序后就会直接从内存里面返回查询结果了，不用再回到原表去取数据。</p>
<p>这也就体现了 MySQL 的一个设计思想：<strong>如果内存够，就要多利用内存，尽量减少磁盘访问。</strong></p>
<p>对于 InnoDB 表来说，rowid 排序会要求回表多造成磁盘读，因此不会被优先选择。</p>
<p>这个结论看上去有点废话的感觉，但是你要记住它，下一篇文章我们就会用到。</p>
<p>看到这里，你就了解了，MySQL 做排序是一个成本比较高的操作。那么你会问，是不是所有的 order by 都需要排序操作呢？如果不排序就能得到正确的结果，那对系统的消耗会小很多，语句的执行时间也会变得更短。</p>
<p>其实，并不是所有的 order by 语句，都需要排序操作的。从上面分析的执行过程，我们可以看到，MySQL 之所以需要生成临时表，并且在临时表上做排序操作，<strong>其原因是原来的数据都是无序的。</strong></p>
<p>你可以设想下，如果能够保证从 city 这个索引上取出来的行，天然就是按照 name 递增排序的话，是不是就可以不用再排序了呢？</p>
<p>确实是这样的。</p>
<p>所以，我们可以在这个市民表上创建一个 city 和 name 的联合索引，对应的 SQL 语句是：</p>
<pre><code>alter table t add index city_user(city, name);
</code></pre>
<p>作为与 city 索引的对比，我们来看看这个索引的示意图。</p>
<p><img src="assets/f980201372b676893647fb17fac4e2bf.png" alt="img" /></p>
<p>图 7 city 和 name 联合索引示意图</p>
<p>在这个索引里面，我们依然可以用树搜索的方式定位到第一个满足 city='杭州’的记录，并且额外确保了，接下来按顺序取“下一条记录”的遍历过程中，只要 city 的值是杭州，name 的值就一定是有序的。</p>
<p>这样整个查询过程的流程就变成了：</p>
<ol>
<li>从索引 (city,name) 找到第一个满足 city='杭州’条件的主键 id；</li>
<li>到主键 id 索引取出整行，取 name、city、age 三个字段的值，作为结果集的一部分直接返回；</li>
<li>从索引 (city,name) 取下一个记录主键 id；</li>
<li>重复步骤 2、3，直到查到第 1000 条记录，或者是不满足 city='杭州’条件时循环结束。</li>
</ol>
<p><img src="assets/3f590c3a14f9236f2d8e1e2cb9686692.jpg" alt="img" /></p>
<p>图 8 引入 (city,name) 联合索引后，查询语句的执行计划</p>
<p>可以看到，这个查询过程不需要临时表，也不需要排序。接下来，我们用 explain 的结果来印证一下。</p>
<p><img src="assets/fc53de303811ba3c46d344595743358a.png" alt="img" /></p>
<p>图 9 引入 (city,name) 联合索引后，查询语句的执行计划</p>
<p>从图中可以看到，Extra 字段中没有 Using filesort 了，也就是不需要排序了。而且由于 (city,name) 这个联合索引本身有序，所以这个查询也不用把 4000 行全都读一遍，只要找到满足条件的前 1000 条记录就可以退出了。也就是说，在我们这个例子里，只需要扫描 1000 次。</p>
<p>既然说到这里了，我们再往前讨论，**这个语句的执行流程有没有可能进一步简化呢？**不知道你还记不记得，我在第 5 篇文章[《 深入浅出索引（下）》]中，和你介绍的覆盖索引。</p>
<p>这里我们可以再稍微复习一下。<strong>覆盖索引是指，索引上的信息足够满足查询请求，不需要再回到主键索引上去取数据。</strong></p>
<p>按照覆盖索引的概念，我们可以再优化一下这个查询语句的执行流程。</p>
<p>针对这个查询，我们可以创建一个 city、name 和 age 的联合索引，对应的 SQL 语句就是：</p>
<pre><code>alter table t add index city_user_age(city, name, age);
</code></pre>
<p>这时，对于 city 字段的值相同的行来说，还是按照 name 字段的值递增排序的，此时的查询语句也就不再需要排序了。这样整个查询语句的执行流程就变成了：</p>
<ol>
<li>从索引 (city,name,age) 找到第一个满足 city='杭州’条件的记录，取出其中的 city、name 和 age 这三个字段的值，作为结果集的一部分直接返回；</li>
<li>从索引 (city,name,age) 取下一个记录，同样取出这三个字段的值，作为结果集的一部分直接返回；</li>
<li>重复执行步骤 2，直到查到第 1000 条记录，或者是不满足 city='杭州’条件时循环结束。</li>
</ol>
<p><img src="assets/df4b8e445a59c53df1f2e0f115f02cd6.jpg" alt="img" /></p>
<p>图 10 引入 (city,name,age) 联合索引后，查询语句的执行流程</p>
<p>然后，我们再来看看 explain 的结果。</p>
<p><img src="assets/9e40b7b8f0e3f81126a9171cc22e3423.png" alt="img" /></p>
<p>图 11 引入 (city,name,age) 联合索引后，查询语句的执行计划</p>
<p>可以看到，Extra 字段里面多了“Using index”，表示的就是使用了覆盖索引，性能上会快很多。</p>
<p>当然，这里并不是说要为了每个查询能用上覆盖索引，就要把语句中涉及的字段都建上联合索引，毕竟索引还是有维护代价的。这是一个需要权衡的决定。</p>
<h1>小结</h1>
<p>今天这篇文章，我和你介绍了 MySQL 里面 order by 语句的几种算法流程。</p>
<p>在开发系统的时候，你总是不可避免地会使用到 order by 语句。你心里要清楚每个语句的排序逻辑是怎么实现的，还要能够分析出在最坏情况下，每个语句的执行对系统资源的消耗，这样才能做到下笔如有神，不犯低级错误。</p>
<p>最后，我给你留下一个思考题吧。</p>
<p>假设你的表里面已经有了 city_name(city, name) 这个联合索引，然后你要查杭州和苏州两个城市中所有的市民的姓名，并且按名字排序，显示前 100 条记录。如果 SQL 查询语句是这么写的 ：</p>
<pre><code>mysql&gt; select * from t where city in ('杭州',&quot; 苏州 &quot;) order by name limit 100;
</code></pre>
<p>那么，这个语句执行的时候会有排序过程吗，为什么？</p>
<p>如果业务端代码由你来开发，需要实现一个在数据库端不需要排序的方案，你会怎么实现呢？</p>
<p>进一步地，如果有分页需求，要显示第 101 页，也就是说语句最后要改成 “limit 10000,100”， 你的实现方法又会是什么呢？</p>
<p>你可以把你的思考和观点写在留言区里，我会在下一篇文章的末尾和你讨论这个问题。感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。</p>
<h1>上期问题时间</h1>
<p>上期的问题是，当 MySQL 去更新一行，但是要修改的值跟原来的值是相同的，这时候 MySQL 会真的去执行一次修改吗？还是看到值相同就直接返回呢？</p>
<p>这是第一次我们课后问题的三个选项都有同学选的，所以我要和你需要详细说明一下。</p>
<p>第一个选项是，MySQL 读出数据，发现值与原来相同，不更新，直接返回，执行结束。这里我们可以用一个锁实验来确认。</p>
<p>假设，当前表 t 里的值是 (1,2)。</p>
<p><img src="assets/6d9d8837560d01b57d252c470157ea90.png" alt="img" /></p>
<p>图 12 锁验证方式</p>
<p>session B 的 update 语句被 blocked 了，加锁这个动作是 InnoDB 才能做的，所以排除选项 1。</p>
<p>第二个选项是，MySQL 调用了 InnoDB 引擎提供的接口，但是引擎发现值与原来相同，不更新，直接返回。有没有这种可能呢？这里我用一个可见性实验来确认。</p>
<p>假设当前表里的值是 (1,2)。</p>
<p><img src="assets/441682b64a3f5dd50f35b12ca4b87c96.png" alt="img" /></p>
<p>图 13 可见性验证方式</p>
<p>session A 的第二个 select 语句是一致性读（快照读)，它是不能看见 session B 的更新的。</p>
<p>现在它返回的是 (1,3)，表示它看见了某个新的版本，这个版本只能是 session A 自己的 update 语句做更新的时候生成。（如果你对这个逻辑有疑惑的话，可以回顾下第 8 篇文章[《事务到底是隔离的还是不隔离的？》]中的相关内容）</p>
<p>所以，我们上期思考题的答案应该是选项 3，即：InnoDB 认真执行了“把这个值修改成 (1,2)&quot;这个操作，该加锁的加锁，该更新的更新。</p>
<p>然后你会说，MySQL 怎么这么笨，就不会更新前判断一下值是不是相同吗？如果判断一下，不就不用浪费 InnoDB 操作，多去更新一次了？</p>
<p>其实 MySQL 是确认了的。只是在这个语句里面，MySQL 认为读出来的值，只有一个确定的 (id=1), 而要写的是 (a=3)，只从这两个信息是看不出来“不需要修改”的。</p>
<p>作为验证，你可以看一下下面这个例子。</p>
<p><img src="assets/63dd6df32dacdb827d256e5acb9837c1.png" alt="img" /></p>
<p>图 14 可见性验证方式 -- 对照</p>
<p><strong>补充说明：</strong></p>
<p>上面我们的验证结果都是在 binlog_format=statement 格式下进行的。</p>
<p>@didiren 补充了一个 case， 如果是 binlog_format=row 并且 binlog_row_image=FULL 的时候，由于 MySQL 需要在 binlog 里面记录所有的字段，所以在读数据的时候就会把所有数据都读出来了。</p>
<p>根据上面说的规则，“既然读了数据，就会判断”， 因此在这时候，select * from t where id=1，结果就是“返回 (1,2)”。</p>
<p>同理，如果是 binlog_row_image=NOBLOB, 会读出除 blob 外的所有字段，在我们这个例子里，结果还是“返回 (1,2)”。</p>
<p>对应的代码如图 15 所示。这是 MySQL 5.6 版本引入的，在此之前我没有看过。所以，特此说明。</p>
<p><img src="assets/d413b9235d56c62f9829750a68b06b89.png" alt="img" /></p>
<p>图 15 binlog_row_image=FULL 读字段逻辑</p>
<p>类似的，@mahonebags 同学提到了 timestamp 字段的问题。结论是：如果表中有 timestamp 字段而且设置了自动更新的话，那么更新“别的字段”的时候，MySQL 会读入所有涉及的字段，这样通过判断，就会发现不需要修改。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;答疑文章（一）：日志和索引相关问题.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;如何正确地显示随机消息？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4347268aaf70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
