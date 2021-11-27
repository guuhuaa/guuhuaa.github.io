<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05 Redis 持久化——混合持久化.md</title>
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

                    <a class="current-tab" href="05&#32;Redis&#32;持久化——混合持久化.md">05 Redis 持久化——混合持久化.md</a>
                    

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
                        <div><h1>05 Redis 持久化——混合持久化</h1>
<p>RDB 和 AOF 持久化各有利弊，RDB 可能会导致一定时间内的数据丢失，而 AOF 由于文件较大则会影响 Redis 的启动速度，为了能同时使用 RDB 和 AOF 各种的优点，Redis 4.0 之后新增了混合持久化的方式。</p>
<p>在开启混合持久化的情况下，AOF 重写时会把 Redis 的持久化数据，以 RDB 的格式写入到 AOF 文件的开头，之后的数据再以 AOF 的格式化追加的文件的末尾。</p>
<p>混合持久化的数据存储结构如下图所示： <img src="assets/2020-02-24-122549.png" alt="image.png" /></p>
<h3>1 开启混合持久化</h3>
<p>查询是否开启混合持久化可以使用 <code>config get aof-use-rdb-preamble</code> 命令，执行结果如下图所示： <img src="assets/2020-02-24-122552.png" alt="image.png" /> 其中 yes 表示已经开启混合持久化，no 表示关闭，Redis 5.0 默认值为 yes。 如果是其他版本的 Redis 首先需要检查一下，是否已经开启了混合持久化，如果关闭的情况下，可以通过以下两种方式开启：</p>
<ul>
<li>通过命令行开启</li>
<li>通过修改 Redis 配置文件开启</li>
</ul>
<h4>1）通过命令行开启</h4>
<p>使用命令 <code>config set aof-use-rdb-preamble yes</code> 执行结果如下图所示： <img src="assets/2020-02-24-122553.png" alt="image.png" /></p>
<blockquote>
<p>小贴士：命令行设置配置的缺点是重启 Redis 服务之后，设置的配置就会失效。</p>
</blockquote>
<h4>2）通过修改 Redis 配置文件开启</h4>
<p>在 Redis 的根路径下找到 redis.conf 文件，把配置文件中的 <code>aof-use-rdb-preamble no</code> 改为 <code>aof-use-rdb-preamble yes</code> 如下图所示： <img src="assets/2020-02-24-122555.png" alt="image.png" /></p>
<h3>2 实例运行</h3>
<p>当在混合持久化关闭的情况下，使用 <code>bgrewriteaof</code> 触发 AOF 文件重写之后，查看 appendonly.aof 文件的持久化日志，如下图所示： <img src="assets/2020-02-24-122556.png" alt="image.png" /> 可以看出，当混合持久化关闭的情况下 AOF 持久化文件存储的为标准的 AOF 格式的文件。 当混合持久化开启的模式下，使用 <code>bgrewriteaof</code> 命令触发 AOF 文件重写，得到 appendonly.aof 的文件内容如下图所示： <img src="assets/2020-02-24-122557.png" alt="image.png" /> 可以看出 appendonly.aof 文件存储的内容是 <code>REDIS</code> 开头的 RDB 格式的内容，并非为 AOF 格式的日志。</p>
<h3>3 数据恢复和源码解析</h3>
<p>混合持久化的数据恢复和 AOF 持久化过程是一样的，只需要把 appendonly.aof 放到 Redis 的根目录，在 Redis 启动时，只要开启了 AOF 持久化，Redis 就会自动加载并恢复数据。 Redis 启动信息如下图所示： <img src="assets/2020-02-24-122558.png" alt="image.png" /> 可以看出 Redis 在服务器初始化的时候加载了 AOF 文件的内容。</p>
<h4>1）混合持久化的加载流程</h4>
<p>混合持久化的加载流程如下：</p>
<ol>
<li>判断是否开启 AOF 持久化，开启继续执行后续流程，未开启执行加载 RDB 文件的流程；</li>
<li>判断 appendonly.aof 文件是否存在，文件存在则执行后续流程；</li>
<li>判断 AOF 文件开头是 RDB 的格式, 先加载 RDB 内容再加载剩余的 AOF 内容；</li>
<li>判断 AOF 文件开头不是 RDB 的格式，直接以 AOF 格式加载整个文件。</li>
</ol>
<p>AOF 加载流程图如下图所示： <img src="assets/2020-02-24-122601.png" alt="image.png" /> 2）源码解析</p>
<p>Redis 判断 AOF 文件的开头是否是 RDB 格式的，是通过关键字 <code>REDIS</code> 判断的，RDB 文件的开头一定是 <code>REDIS</code> 关键字开头的，判断源码在 Redis 的 src/aof.c 中，核心代码如下所示：</p>
<pre><code class="language-c">char sig[5]; /* &quot;REDIS&quot; */
if (fread(sig,1,5,fp) != 5 || memcmp(sig,&quot;REDIS&quot;,5) != 0) {
    // AOF 文件开头非 RDB 格式，非混合持久化文件
    if (fseek(fp,0,SEEK_SET) == -1) goto readerr;
} else {
    /* RDB preamble. Pass loading the RDB functions. */
    rio rdb;

    serverLog(LL_NOTICE,&quot;Reading RDB preamble from AOF file...&quot;);
    if (fseek(fp,0,SEEK_SET) == -1) goto readerr;
    rioInitWithFile(&amp;rdb,fp);
    // AOF 文件开头是 RDB 格式，先加载 RDB 再加载 AOF
    if (rdbLoadRio(&amp;rdb,NULL,1) != C_OK) {
        serverLog(LL_WARNING,&quot;Error reading the RDB preamble of the AOF file, AOF loading aborted&quot;);
        goto readerr;
    } else {
        serverLog(LL_NOTICE,&quot;Reading the remaining AOF tail...&quot;);
    }
}
// 加载 AOF 格式的数据

</code></pre>
<p>可以看出 Redis 是通过判断 AOF 文件的开头是否是 <code>REDIS</code> 关键字，来确定此文件是否为混合持久化文件的。</p>
<blockquote>
<p>小贴士：AOF 格式的开头是 *，而 RDB 格式的开头是 REDIS。</p>
</blockquote>
<h3>4 优缺点</h3>
<p><strong>混合持久化优点：</strong></p>
<ul>
<li>混合持久化结合了 RDB 和 AOF 持久化的优点，开头为 RDB 的格式，使得 Redis 可以更快的启动，同时结合 AOF 的优点，有减低了大量数据丢失的风险。</li>
</ul>
<p><strong>混合持久化缺点：</strong></p>
<ul>
<li>AOF 文件中添加了 RDB 格式的内容，使得 AOF 文件的可读性变得很差；</li>
<li>兼容性差，如果开启混合持久化，那么此混合持久化 AOF 文件，就不能用在 Redis 4.0 之前版本了。</li>
</ul>
<h3>5 持久化最佳实践</h3>
<p>持久化虽然保证了数据不丢失，但同时拖慢了 Redis 的运行速度，那怎么更合理的使用 Redis 的持久化功能呢？ Redis 持久化的最佳实践可从以下几个方面考虑。</p>
<h4>1）控制持久化开关</h4>
<p>使用者可根据实际的业务情况考虑，如果对数据的丢失不敏感的情况下，可考虑关闭 Redis 的持久化，这样所以的键值操作都在内存中，就可以保证最高效率的运行 Redis 了。 持久化关闭操作：</p>
<ul>
<li>关闭 RDB 持久化，使用命令： <code>config set save &quot;&quot;</code></li>
<li>关闭 AOF 和 混合持久化，使用命令： <code>config set appendonly no</code></li>
</ul>
<h4>2）主从部署</h4>
<p>使用主从部署，一台用于响应主业务，一台用于数据持久化，这样就可能让 Redis 更加高效的运行。</p>
<h4>3）使用混合持久化</h4>
<p>混合持久化结合了 RDB 和 AOF 的优点，Redis 5.0 默认是开启的。</p>
<h4>4）使用配置更高的机器</h4>
<p>Redis 对 CPU 的要求并不高，反而是对内存和磁盘的要求很高，因为 Redis 大部分时候都在做读写操作，使用更多的内存和更快的磁盘，对 Redis 性能的提高非常有帮助。</p>
<p><strong>参考&amp;鸣谢</strong> <a href="https://redis.io/topics/persistence">https://redis.io/topics/persistence</a> <a href="https://blog.csdn.net/qq_36318234/article/details/79994133">https://blog.csdn.net/qq_36318234/article/details/79994133</a> <a href="https://www.cnblogs.com/wdliu/p/9377278.html">https://www.cnblogs.com/wdliu/p/9377278.html</a></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;Redis&#32;持久化——AOF.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;字符串使用与内部实现原理.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4349c47cdc70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
