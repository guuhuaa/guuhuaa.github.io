<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17 Redis 键值过期操作.md</title>
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

                    <a class="current-tab" href="17&#32;Redis&#32;键值过期操作.md">17 Redis 键值过期操作.md</a>
                    

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
                        <div><h1>17 Redis 键值过期操作</h1>
<h3>过期设置</h3>
<p>Redis 中设置过期时间主要通过以下四种方式：</p>
<ul>
<li>expire key seconds：设置 key 在 n 秒后过期；</li>
<li>pexpire key milliseconds：设置 key 在 n 毫秒后过期；</li>
<li>expireat key timestamp：设置 key 在某个时间戳（精确到秒）之后过期；</li>
<li>pexpireat key millisecondsTimestamp：设置 key 在某个时间戳（精确到毫秒）之后过期；</li>
</ul>
<p>下面分别来看以上这些命令的具体实现。</p>
<h4><strong>expire：N 秒后过期</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; set key value
OK
127.0.0.1:6379&gt; expire key 100
(integer) 1
127.0.0.1:6379&gt; ttl key
(integer) 97

</code></pre>
<p>其中命令 ttl 的全称是 Time To Live，表示此键值在 n 秒后过期。例如，上面的结果 97 表示 key 在 97s 后过期。</p>
<h4><strong>pexpire：N 毫秒后过期</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; set key2 value2
OK
127.0.0.1:6379&gt; pexpire key2 100000
(integer) 1
127.0.0.1:6379&gt; pttl key2
(integer) 94524

</code></pre>
<p>其中 <code>pexpire key2 100000</code> 表示设置 key2 在 100000 毫秒（100 秒）后过期。</p>
<h4><strong>expireat：过期时间戳精确到秒</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; set key3 value3
OK
127.0.0.1:6379&gt; expireat key3 1573472683
(integer) 1
127.0.0.1:6379&gt; ttl key3
(integer) 67

</code></pre>
<p>其中 <code>expireat key3 1573472683</code> 表示 key3 在时间戳 1573472683 后过期（精确到秒），使用 ttl 查询可以发现在 67s 后 key3 会过期。</p>
<blockquote>
<p>小贴士：在 Redis 可以使用 time 命令查询当前时间的时间戳（精确到秒），示例如下：</p>
<p>127.0.0.1:6379&gt; time</p>
<ol>
<li>
<p>&quot;1573472563&quot;</p>
</li>
<li>
<p>&quot;248426&quot;</p>
</li>
</ol>
</blockquote>
<h4><strong>pexpireat：过期时间戳精确到毫秒</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; set key4 value4
OK
127.0.0.1:6379&gt; pexpireat key4 1573472683000
(integer) 1
127.0.0.1:6379&gt; pttl key4
(integer) 3522

</code></pre>
<p>其中 <code>pexpireat key4 1573472683000</code> 表示 key4 在时间戳 1573472683000 后过期（精确到毫秒），使用 ttl 查询可以发现在 3522ms 后 key4 会过期。</p>
<h4><strong>字符串中的过期操作</strong></h4>
<p>字符串中几个直接操作过期时间的方法，如下列表：</p>
<ul>
<li>set key value ex seconds：设置键值对的同时指定过期时间（精确到秒）；</li>
<li>set key value px milliseconds：设置键值对的同时指定过期时间（精确到毫秒）；</li>
<li>setex key seconds valule：设置键值对的同时指定过期时间（精确到秒）。</li>
</ul>
<p>实现示例如下。</p>
<p><strong>1. set key value ex seconds</strong></p>
<pre><code class="language-shell">127.0.0.1:6379&gt; set k v ex 100
OK
127.0.0.1:6379&gt; ttl k
(integer) 97

</code></pre>
<p><strong>2. set key value ex milliseconds</strong></p>
<pre><code class="language-shell">127.0.0.1:6379&gt; set k2 v2 px 100000
OK
127.0.0.1:6379&gt; pttl k2
(integer) 92483

</code></pre>
<p><strong>3. setex key seconds valule</strong></p>
<pre><code class="language-shell">127.0.0.1:6379&gt; setex k3 100 v3
OK
127.0.0.1:6379&gt; ttl k3
(integer) 91

</code></pre>
<h3>移除过期时间</h3>
<p>使用命令： <code>persist key</code> 可以移除键值的过期时间，如下代码所示。</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; ttl k3
(integer) 97
127.0.0.1:6379&gt; persist k3
(integer) 1
127.0.0.1:6379&gt; ttl k3
(integer) -1

</code></pre>
<p>可以看出第一次使用 ttl 查询 k3 会在 97s 后过期，当使用了 persist 命令之后，在查询 k3 的存活时间发现结果是 -1，它表示 k3 永不过期。</p>
<h3>Java实现过期操作</h3>
<p>本文将使用 Jedis 框架来实现对 Redis 过期时间的操作，如下代码所示：</p>
<pre><code class="language-java">public class TTLTest {
    public static void main(String[] args) throws InterruptedException {
        // 创建 Redis 连接
        Jedis jedis = new Jedis(&quot;xxx.xxx.xxx.xxx&quot;, 6379);
        // 设置 Redis 密码(如果没有密码，此行可省略)
        jedis.auth(&quot;xxx&quot;);
        // 存储键值对（默认情况下永不过期）
        jedis.set(&quot;k&quot;, &quot;v&quot;);
        // 查询 TTL（过期时间）
        Long ttl = jedis.ttl(&quot;k&quot;);
        // 打印过期日志
        System.out.println(&quot;过期时间：&quot; + ttl);
        // 设置 100s 后过期
        jedis.expire(&quot;k&quot;, 100);
        // 等待 1s 后执行
        Thread.sleep(1000);
        // 打印过期日志
        System.out.println(&quot;执行 expire 后的 TTL=&quot; + jedis.ttl(&quot;k&quot;));
    }
}

</code></pre>
<p>程序的执行结果为：</p>
<pre><code>过期时间：-1
执行 expire 后的 TTL=99

</code></pre>
<p>可以看出使用 Jedis 来操作 Redis 的过期时间还是很方便的，可直接使用 <code>jedis.ttl(&quot;k&quot;)</code> 查询键值的生存时间，使用 <code>jedis.expire(&quot;k&quot;,seconds)</code> 方法设置过期时间（精确到秒）。</p>
<blockquote>
<p>小贴士：使用 Jedis 之前，先要把 Jedis 引入到程序中，如果使用的是 Maven 项目的，直接在 pom.xml 文件中添加以下引用：</p>
</blockquote>
<pre><code class="language-java">&lt;!-- https://mvnrepository.com/artifact/redis.clients/jedis --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;redis.clients&lt;/groupId&gt;
    &lt;artifactId&gt;jedis&lt;/artifactId&gt;
    &lt;version&gt;version&lt;/version&gt;
&lt;/dependency&gt;

</code></pre>
<p><strong>更多过期操作方法</strong>，如下列表：</p>
<ul>
<li>pexpire(String key, long milliseconds)：设置 n 毫秒后过期；</li>
<li>expireAt(String key, long unixTime)：设置某个时间戳后过期（精确到秒）；</li>
<li>pexpireAt(String key, long millisecondsTimestamp)：设置某个时间戳后过期（精确到毫秒）；</li>
<li>persist(String key)：移除过期时间。</li>
</ul>
<p>完整示例代码如下：</p>
<pre><code class="language-java">public class TTLTest {
    public static void main(String[] args) throws InterruptedException {
        // 创建 Redis 连接
        Jedis jedis = new Jedis(&quot;xxx.xxx.xxx.xxx&quot;, 6379);
        // 设置 Redis 密码(如果没有密码，此行可省略)
        jedis.auth(&quot;xxx&quot;);
        // 存储键值对（默认情况下永不过期）
        jedis.set(&quot;k&quot;, &quot;v&quot;);
        // 查询 TTL（过期时间）
        Long ttl = jedis.ttl(&quot;k&quot;);
        // 打印过期日志
        System.out.println(&quot;过期时间：&quot; + ttl);
        // 设置 100s 后过期
        jedis.expire(&quot;k&quot;, 100);
        // 等待 1s 后执行
        Thread.sleep(1000);
        // 打印过期日志
        System.out.println(&quot;执行 expire 后的 TTL=&quot; + jedis.ttl(&quot;k&quot;));
        // 设置 n 毫秒后过期
        jedis.pexpire(&quot;k&quot;, 100000);
        // 设置某个时间戳后过期（精确到秒）
        jedis.expireAt(&quot;k&quot;, 1573468990);
        // 设置某个时间戳后过期（精确到毫秒）
        jedis.pexpireAt(&quot;k&quot;, 1573468990000L);
        // 移除过期时间
        jedis.persist(&quot;k&quot;);
    }
}

</code></pre>
<h3>持久化中的过期键</h3>
<p>上面我们讲了过期键在 Redis 正常运行中一些使用案例，接下来，我们来看 Redis 在持久化的过程中是如何处理过期键的。</p>
<p>Redis 持久化文件有两种格式：RDB（Redis Database）和 AOF（Append Only File），下面我们分别来看过期键在这两种格式中的呈现状态。</p>
<h4><strong>RDB 中的过期键</strong></h4>
<p>RDB 文件分为两个阶段，RDB 文件生成阶段和加载阶段。</p>
<p><strong>1. RDB 文件生成</strong></p>
<p>从内存状态持久化成 RDB（文件）的时候，会对 key 进行过期检查，过期的键不会被保存到新的 RDB 文件中，因此 Redis 中的过期键不会对生成新 RDB 文件产生任何影响。</p>
<p><strong>2. RDB 文件加载</strong></p>
<p>RDB 加载分为以下两种情况：</p>
<ul>
<li>如果 Redis 是主服务器运行模式的话，在载入 RDB 文件时，程序会对文件中保存的键进行检查，过期键不会被载入到数据库中。所以过期键不会对载入 RDB 文件的主服务器造成影响；</li>
<li>如果 Redis 是从服务器运行模式的话，在载入 RDB 文件时，不论键是否过期都会被载入到数据库中。但由于主从服务器在进行数据同步时，从服务器的数据会被清空。所以一般来说，过期键对载入 RDB 文件的从服务器也不会造成影响。</li>
</ul>
<p>RDB 文件加载的源码可以在 rdb.c 文件的 rdbLoad() 函数中找到，源码所示：</p>
<pre><code class="language-c">/* Check if the key already expired. This function is used when loading
* an RDB file from disk, either at startup, or when an RDB was
* received from the master. In the latter case, the master is
* responsible for key expiry. If we would expire keys here, the
* snapshot taken by the master may not be reflected on the slave. 
*
* 如果服务器为主节点的话，
* 那么在键已经过期的时候，不再将它们关联到数据库中去
*/
if (server.masterhost == NULL &amp;&amp; expiretime != -1 &amp;&amp; expiretime &lt; now) {
    decrRefCount(key);
    decrRefCount(val);
    // 跳过
    continue;
}

</code></pre>
<h4><strong>AOF 中的过期键</strong></h4>
<p><strong>1. AOF 文件写入</strong></p>
<p>当 Redis 以 AOF 模式持久化时，如果数据库某个过期键还没被删除，那么 AOF 文件会保留此过期键，当此过期键被删除后，Redis 会向 AOF 文件追加一条 DEL 命令来显式地删除该键值。</p>
<p><strong>2. AOF 重写</strong></p>
<p>执行 AOF 重写时，会对 Redis 中的键值对进行检查已过期的键不会被保存到重写后的 AOF 文件中，因此不会对 AOF 重写造成任何影响。</p>
<h3>主从库的过期键</h3>
<p>当 Redis 运行在主从模式下时，从库不会进行过期扫描，从库对过期的处理是被动的。也就是即使从库中的 key 过期了，如果有客户端访问从库时，依然可以得到 key 对应的值，像未过期的键值对一样返回。</p>
<p>从库的过期键处理依靠主服务器控制，主库在 key 到期时，会在 AOF 文件里增加一条 del 指令，同步到所有的从库，从库通过执行这条 del 指令来删除过期的 key。</p>
<h3>小结</h3>
<p>本文我们知道了 Redis 中的四种设置过期时间的方式：expire、pexpire、expireat、pexpireat，其中比较常用的是 expire 设置键值 n 秒后过期。</p>
<p>字符串中可以在添加键值的同时设置过期时间，并可以使用 persist 命令移除过期时间。同时我们也知道了过期键在 RDB 写入和 AOF 重写时都不会被记录。</p>
<p>过期键在主从模式下，从库对过期键的处理要完全依靠主库，主库删除过期键之后会发送 del 命令给所有的从库。</p>
<p>本文的知识点，如下图所示：</p>
<p><img src="assets/3e0fac90-5de5-11ea-b393-df0a55152c2b" alt="image.png" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;Redis&#32;事务深入解析.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;Redis&#32;过期策略与源码分析.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a093a4770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
