<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07  表的访问设计：你该选择 SQL 还是 NoSQL？.md</title>
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

                    <a class="current-tab" href="07&#32;&#32;表的访问设计：你该选择&#32;SQL&#32;还是&#32;NoSQL？.md">07  表的访问设计：你该选择 SQL 还是 NoSQL？.md</a>
                    

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

                    
                    <a href="15&#32;&#32;MySQL&#32;复制：最简单也最容易配置出错.md">15  MySQL 复制：最简单也最容易配置出错.md</a>

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
                        <div><h1>07  表的访问设计：你该选择 SQL 还是 NoSQL？</h1>
<p>到目前为止，我已经带你学习了表结构的字段类型选择和表的物理存储设计，这一讲我们将继续学习表的访问选型。这样一来，字段类型选择 + 物理存储设计 + 表的访问设计，就完成了表结构设计的所有内容。</p>
<p>前面 6 讲，我演示的都是通过 SQL 的方式对表进行访问，但从 MySQL 5.6 版本开始，就支持除 SQL 外的其他访问方式，比如 NoSQL，甚至可以把 MySQL 打造成一个百万级并发访问的 KV 数据库或文档数据库。</p>
<p>今天这一讲，我就带你从全局角度看 MySQL 数据库中表的访问方式，以及它们各自的使用场景，希望你能有所收获。</p>
<h3>MySQL 中表的访问方式</h3>
<p>SQL 是访问数据库的一个通用接口，虽然数据库有很多种，但数据库中的 SQL 却是类似的，因为 SQL 有标准存在，如 SQL92、SQL2003 等。</p>
<p>虽然有些数据库会扩展支持 SQL 标准外的语法，但 90% 的语法是兼容的，所以，不同数据库在 SQL 层面的学习成本是比较低的。也因为上述原因，从一种关系型数据库迁移到另一种关系型数据库，开发的迁移成本并不高。比如去 IOE，将 Oracle 数据库迁移到 MySQL 数据库，通常 SQL 语法并不是难题。</p>
<p>MySQL 8.0 版本前，有不少同学会吐槽 MySQL 对于 SQL 标准的支持的程度。但是在当前 8.0 版本下，MySQL 对于 SQL 语法的支持度已经越来越好，甚至在某些方面超过了商业数据库 Oracle。</p>
<p><img src="assets/Cgp9HWCeMqyAb4fUABDbOi8o_AI403.png" alt="Drawing 1.png" /></p>
<p>上图是专家评估的不同数据库对 SQL 的支持程度，可以看到，MySQL 8.0 在这一块非常完善，特别是对 JSON_TABLE 的支持功能。</p>
<p>通常来说，MySQL 数据库用于 OLTP 的在线系统中，不用特别复杂的 SQL 语法支持。但 MySQL 8.0 完备的 SQL 支持意味着 MySQL 未来将逐渐补齐在 OLAP 业务方面的短板，让我们一起拭目以待。</p>
<p>当然，通过 SQL 访问表，你肯定并不陌生，这也不是本讲的重点。<strong>接下来我重点带你了解 MySQL 怎么通过 NoSQL 的方式访问表中的数据。</strong></p>
<p>我们先来看看当前 MySQL 版本中支持的不同表的访问方式：</p>
<p><img src="assets/CioPOWCeMr2AbND9AAMtpbJCKIs777.png" alt="Drawing 3.png" /></p>
<p>MySQL 三种表的访问方式</p>
<p>可以看到，除了标准的 SQL 访问，MySQL 5.6 版本开始还支持通过 Memcached 通信协议访问表中的数据，这时 MySQL 可以作为一个 KV 数据库使用。此外，MySQL 5.7 版本开始还支持通过新的 MySQL X 通信协议访问表中的数据，这时 MySQL 可以作为一个文档数据库使用。</p>
<p>但无论哪种 NoSQL 的访问方式，其访问的数据都是以表的方式进行存储。SQL 和 NoSQL 之间通过某种映射关系进行绑定。</p>
<p>对比传统的 NoSQL 数据库（比如 Memcached、MongoDB），MySQL 这样的访问更具有灵活性，在通过简单的 NoSQL 接口保障性能的前提下，又可以通过 SQL 的方式丰富对于数据的查询。另外，MySQL 提供的成熟事务特性、高可用解决方案，又能弥补 NoSQL 数据库在这方面的不足。</p>
<p>那接下来，我们先来看一看基于 Memcache 协议的 NoSQL 访问方式。</p>
<h3>通过 Memcached 协议访问表</h3>
<p>MySQL 5.6 版本开始支持通过插件 Memcached Plugin，以 KV 方式访问表，这时可以将 MySQL视作一个 Memcached KV 数据库。</p>
<p>对于数据的访问不再是通过 SQL 接口，而是通过 KV 数据库中常见的 get、set、incr 等请求。</p>
<p>但为什么要通过 KV 的方式访问数据呢？因为有些业务对于数据库的访问本质上都是一个 KV 操作。比如用户登录系统，大多是用于信息确认，这时其 SQL 大多都是通过主键或唯一索引进行数据的查询，如：</p>
<pre><code>SELECT * FROM User WHERE PK = ?
</code></pre>
<p>若在海量并发访问的系统中，通过 SQL 访问这些表，由于通过主键索引进行访问，速度很快。但 SQL 解析（哪怕是软解析）却要耗费不少时间，这时单数据库实例性能会受到一定的限制。</p>
<p>基于 Memcached 的 KV 访问，可以绕过 SQL 解析，通过映射关系，直接访问存储在 InnoDB 引擎中的数据，这样数据库的整体性能会在不花费额外成本的前提下得到极大的提升。</p>
<p>那么要启用 Memcached 协议访问 MySQL 需要做两件事情：</p>
<ul>
<li>开启 Memcached 插件；</li>
<li>配置表与 KV 的映射关系。</li>
</ul>
<p>具体操作如下所示：</p>
<pre><code>-- 安装映射表

mysql&gt; source MYSQL_HOME/share/innodb_memcached_config.sql



-- 安装插件，默认会启动11211端口

mysql&gt; INSTALL PLUGIN daemon_memcached soname &quot;libmemcached.so&quot;;
</code></pre>
<p>执行完上述操作后，会新增一个库 innodb_memcache，里面的表 containers 就是需要配置的KV映射表。如果业务常见的主键查询 SQL 如下，其中列 user_id 是主键：</p>
<pre><code>SELECT user_id,cellphone,last_login 

FROM test.User 

WHERE user_id = ？
</code></pre>
<p>那么我们可以在表 Containers 中插入一条记录：</p>
<pre><code>INSERT INTO containers

VALUES ('User','test','user_id','user_id|cellphone|last_login','0','0','0','PRIAMRY')
</code></pre>
<p>上面的映射关系表示通过 Memcached 的 KV 方式访问，其本质是通过 PRIAMRY 索引访问 key 值，key 就是 user_id，value 值返回的是由列 user_id、cellphone、last_login 组合而成，分隔符为&quot;|&quot;的字符串。</p>
<p>最后，通过 SQL 和 KV 的对比性能测试，可以发现通过 KV 的方式访问，性能要好非常多，在我的测试服务器上结果如下所示：</p>
<p><img src="assets/Cgp9HWCeMtOAFN_LAAJjGPv67qw823.png" alt="Drawing 5.png" /></p>
<p>从测试结果可以看到，<strong>基于 Memcached 的 KV 访问方式比传统的 SQL 方式要快54.33%</strong>，而且CPU 的开销反而还要低20%。</p>
<p>当然了，上述操作只是将表 User 作为 KV 访问，如果想将其他表通过 KV 的方式访问，可以继续在表 Containers 中进行配置。但是在使用时，务必先通过 GET 命令指定要访问的表：</p>
<pre><code># Python伪代码

mc = Client('127.0.0.1:11211')

mc.get('@@User') # 读取映射表User

mc.get('key1')

mc.get('@@sbtest1') # 读取映射表sbtest1

mc.set('sb1_key1','aa|bbb|ccc')

......
</code></pre>
<p>另一种使用 Memcached Plugin 的场景是原先使用原生 Memcached KV 数据库的用户。这些用户可以考虑将 Memcached 数据库迁移到 MySQL 。这样的好处是：</p>
<ul>
<li>通过 MySQL 进行访问的性能比原生 Memcached 好，数据库并发优化做得更好；</li>
<li>存储可以持久化，支持事务，数据一致性和安全性更好；</li>
<li>利用 MySQL 复制技术，可以弥补原生 Memcached 不支持数据复制的短板；</li>
</ul>
<h3>通过 X Protocol 访问表</h3>
<p>MySQL 5.7 版本开始原生支持 JSON 二进制数据类型，同时也提供将表格映射为一个 JSON 文档。同时，MySQL 也提供了 X Protocol 这样的 NoSQL 访问方式，所以，现在我们 MySQL 打造成一个<strong>SQL &amp; NoSQL</strong>的文档数据库。</p>
<p>对比 MongoDB 文档数据库，将 MySQL 打造为文档数据库与 MongoDB 的对比在于：</p>
<p><img src="assets/CioPOWCeMuOAEmp2AAEcRizN53k843.png" alt="Drawing 6.png" /></p>
<p>可以看到，除了 MySQL 目前还无法支持数据分片功能外，其他方面 MySQL 的优势会更大一些，特别是 MySQL 是通过二维表格存储 JSON 数据，从而实现文档数据库功能。这样可以通过 SQL 进行很多复杂维度的查询，特别是结合 MySQL 8.0 的 CTE（Common Table Expression）、窗口函数（Window Function）等功能，而这在 MongoDB 中是无法原生实现的。</p>
<p>另外，和 Memcached Plugin 不同的是，MySQL 默认会自动启用 X Plugin 插件，接着就可以通过新的 X Protocol 协议访问 MySQL 中的数据，默认端口 33060，你可以通过下面命令查看有关 X Plugin 的配置：</p>
<pre><code>mysql&gt; SHOW VARIABLES LIEK '%mysqlx%';

+-----------------------------------+--------------------+

| Variable_name                     | Value              |

+-----------------------------------+--------------------+

| mysqlx_bind_address               | *                  |

| mysqlx_compression_algorithms     | 

DEFLATE_STREAM,LZ4_MESSAGE,ZSTD_STREAM                   |

| mysqlx_connect_timeout            | 30                 |

| mysqlx_document_id_unique_prefix  | 0                  |

| mysqlx_enable_hello_notice        | ON                 |

| mysqlx_idle_worker_thread_timeout | 60                 |

| mysqlx_interactive_timeout        | 28800              |

| mysqlx_max_allowed_packet         | 67108864           |

| mysqlx_max_connections            | 100                |

| mysqlx_min_worker_threads         | 2                  |

| mysqlx_port                       | 33060              |

| mysqlx_port_open_timeout          | 0                  |

| mysqlx_read_timeout               | 30                 |

| mysqlx_socket                     | /tmp/mysqlx.sock   |

......
</code></pre>
<p>要通过 X Protocol 管理 MySQL 需要通过新的 MySQL Shell 命令，默认并不安装，需要单独安装。下载地址：<a href="https://dev.mysql.com/downloads/shell/?fileGuid=xxQTRXtVcqtHK6j8">https://dev.mysql.com/downloads/shell/</a>。安装后就可以通过命令 mysqlsh 通过新的 X Protocol 访问 MySQL 数据库：</p>
<pre><code><a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="88fae7e7fcc8c5cad8a5dfe1e6ece7fffb">[email&#160;protected]</a>:# mysqlsh <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4634292932062a2925272a2e293532">[email&#160;protected]</a>/test
</code></pre>
<p>X Protocol 协议支持通过 JS、Python、SQL 的方式管理和访问 MySQL，具体操作你可以参见官方文档。</p>
<p><img src="assets/CioPOWCeMvKAB2VRAALFfWeJmnA003.png" alt="Drawing 8.png" /></p>
<p>开发同学若要通过 X Protocol 协议管理文档数据，也需要下载新的 MySQL Connector，并引入新的 X 驱动库，如 Python 驱动：</p>
<pre><code>import mysqlx



# Connect to server on localhost

session = mysqlx.get_session({

    'host': 'localhost',

    'port': 33060

})



schema = session.get_schema('test')



# Use the collection 'my_collection'

collection = schema.get_collection('my_collection')



# Specify which document to find with Collection.find()

result = collection.find('name like :param').bind('param', 'S%').limit(1).execute()



# Print document

docs = result.fetch_all()

print('Name: {0}'.format(docs[0]['name']))

session.close()
</code></pre>
<h3>总结</h3>
<p>这一讲我带你了解了通过 SQL、Memcache 协议、X Protocol 访问 MySQL 中的表，即我们可以将 MySQL 打造成一个关系型数据库、KV 数据库、文档数据库，但底层都是通过表格的方式进行数据的存储，并且数据都存储在 InnoDB 引擎中。</p>
<p>还在使用 Memcached、MongoDB 数据库的同学可以考虑将数据迁移到 MySQL，这样能在兼容原有业务的前提下，使用到 InnoDB 存储引擎的高并发、事务安全、数据复制等高级功能。</p>
<p>或许有同学会问为什么 KV 数据库、文档数据库不单独使用额外的数据库呢？这是因为在企业的数据中心部门，会要求尽可能的收敛技术栈。这样对后续技术架构的稳定性，人员培养，长远来看，会有更大的收益。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;&#32;表压缩：不仅仅是空间压缩.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;&#32;索引：排序的艺术.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4348127f0b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
