<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>41 案例：Redis 问题汇总和相关解决方案.md</title>
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

                    <a class="current-tab" href="41&#32;案例：Redis&#32;问题汇总和相关解决方案.md">41 案例：Redis 问题汇总和相关解决方案.md</a>
                    

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
                        <div><h1>41 案例：Redis 问题汇总和相关解决方案</h1>
<p>本文收集了一些 Redis 使用中经常遇到的一些问题，和与之相对应的解决方案，这些内容不但会出现在实际工作中，也是面试的高频问题，接下来一起来看。</p>
<h3>缓存雪崩</h3>
<p>缓存雪崩是指在短时间内，有大量缓存同时过期，导致大量的请求直接查询数据库，从而对数据库造成了巨大的压力，严重情况下可能会导致数据库宕机的情况叫做缓存雪崩。</p>
<p>我们先来看下正常情况下和缓存雪崩时程序的执行流程图，正常情况下系统的执行流程如下图所示：</p>
<p><img src="assets/babffe50-8ede-11ea-8e9a-9bc3d95576e7" alt="正常访问图片.png" /></p>
<p>缓存雪崩的执行流程，如下图所示：</p>
<p><img src="assets/c7244bb0-8ede-11ea-a326-c7ef51ab79ae" alt="缓存雪崩.png" /></p>
<p>以上对比图可以看出缓存雪崩对系统造成的影响，那如何解决缓存雪崩的问题？</p>
<p>缓存雪崩的<strong>常用解决方案</strong>有以下几个。</p>
<h4><strong>加锁排队</strong></h4>
<p>加锁排队可以起到缓冲的作用，防止大量的请求同时操作数据库，但它的缺点是增加了系统的响应时间，降低了系统的吞吐量，牺牲了一部分用户体验。</p>
<p>加锁排队的代码实现，如下所示：</p>
<pre><code class="language-java">// 缓存 key
String cacheKey = &quot;userlist&quot;;
// 查询缓存
String data = jedis.get(cacheKey);
if (StringUtils.isNotBlank(data)) {
    // 查询到数据，直接返回结果
    return data;
} else {
    // 先排队查询数据库，在放入缓存
    synchronized (cacheKey) {
        data = jedis.get(cacheKey);
        if (!StringUtils.isNotBlank(data)) { // 双重判断
            // 查询数据库
            data = findUserInfo();
            // 放入缓存
            jedis.set(cacheKey, data);
        }
        return data;
    }
}

</code></pre>
<p>以上为加锁排队的实现示例，读者可根据自己的实际项目情况做相应的修改。</p>
<h4><strong>随机化过期时间</strong></h4>
<p>为了避免缓存同时过期，可在设置缓存时添加随机时间，这样就可以极大的避免大量的缓存同时失效。</p>
<p>示例代码如下：</p>
<pre><code class="language-java">// 缓存原本的失效时间
int exTime = 10 * 60;
// 随机数生成类
Random random = new Random();
// 缓存设置
jedis.setex(cacheKey, exTime+random.nextInt(1000) , value);

</code></pre>
<h4><strong>设置二级缓存</strong></h4>
<p>二级缓存指的是除了 Redis 本身的缓存，再设置一层缓存，当 Redis 失效之后，先去查询二级缓存。</p>
<p>例如可以设置一个本地缓存，在 Redis 缓存失效的时候先去查询本地缓存而非查询数据库。</p>
<p>加入二级缓存之后程序执行流程，如下图所示：</p>
<p><img src="assets/dc14dc60-8ede-11ea-adbb-dd8e7664c503" alt="image.png" /></p>
<h3>缓存穿透</h3>
<p>缓存穿透是指查询数据库和缓存都无数据，因为数据库查询无数据，出于容错考虑，不会将结果保存到缓存中，因此每次请求都会去查询数据库，这种情况就叫做缓存穿透。</p>
<p>缓存穿透执行流程如下图所示：</p>
<p><img src="assets/eb1fb8b0-8ede-11ea-8b41-0f0ef087610d" alt="缓存雪崩-缓存穿透.png" /></p>
<p>其中红色路径表示缓存穿透的执行路径，可以看出缓存穿透会给数据库造成很大的压力。</p>
<p>缓存穿透的解决方案有以下几个。</p>
<h4><strong>使用过滤器</strong></h4>
<p>我们可以使用过滤器来减少对数据库的请求，例如使用我们前面章节所学的布隆过滤器，我们这里简单复习一下布隆过滤器，它的原理是将数据库的数据哈希到 bitmap 中，每次查询之前，先使用布隆过滤器过滤掉一定不存在的无效请求，从而避免了无效请求给数据库带来的查询压力。</p>
<h4><strong>缓存空结果</strong></h4>
<p>另一种方式是我们可以把每次从数据库查询的数据都保存到缓存中，为了提高前台用户的使用体验 (解决长时间内查询不到任何信息的情况)，我们可以将空结果的缓存时间设置得短一些，例如 3~5 分钟。</p>
<h3>缓存击穿</h3>
<p>缓存击穿指的是某个热点缓存，在某一时刻恰好失效了，然后此时刚好有大量的并发请求，此时这些请求将会给数据库造成巨大的压力，这种情况就叫做缓存击穿。</p>
<p>缓存击穿的执行流程如下图所示：</p>
<p><img src="assets/008b1eb0-8edf-11ea-bf74-150f7ff6235d" alt="image.png" /></p>
<p>它的解决方案有以下 2 个。</p>
<h4><strong>加锁排队</strong></h4>
<p>此处理方式和缓存雪崩加锁排队的方法类似，都是在查询数据库时加锁排队，缓冲操作请求以此来减少服务器的运行压力。</p>
<h4><strong>设置永不过期</strong></h4>
<p>对于某些热点缓存，我们可以设置永不过期，这样就能保证缓存的稳定性，但需要注意在数据更改之后，要及时更新此热点缓存，不然就会造成查询结果的误差。</p>
<h3>缓存预热</h3>
<p>首先来说，缓存预热并不是一个问题，而是使用缓存时的一个优化方案，它可以提高前台用户的使用体验。</p>
<p>缓存预热指的是在系统启动的时候，先把查询结果预存到缓存中，以便用户后面查询时可以直接从缓存中读取，以节约用户的等待时间。</p>
<p>缓存预热的执行流程，如下图所示：</p>
<p><img src="assets/10ce2ce0-8edf-11ea-a141-a13a4f8833dd" alt="image.png" /></p>
<p>缓存预热的实现思路有以下三种：</p>
<ol>
<li>把需要缓存的方法写在系统初始化的方法中，这样系统在启动的时候就会自动的加载数据并缓存数据；</li>
<li>把需要缓存的方法挂载到某个页面或后端接口上，手动触发缓存预热；</li>
<li>设置定时任务，定时自动进行缓存预热。</li>
</ol>
<h3>小结</h3>
<p>本文介绍了缓存雪崩产生的原因是因为短时间内大量缓存同时失效，而导致大量请求直接查询数据库的情况，解决方案是加锁、随机设置过期时间和设置二级缓存等；还介绍了查询数据库无数据时会导致的每次空查询都不走缓存的缓存穿透问题，解决方案是使用布隆过滤器和缓存空结果等；同时还介绍了缓存在某一个高并发时刻突然失效导致的缓存击穿问题，以及解决方案——加锁、设置永不过期等方案，最后还介绍了优化系统性能的手段缓存预热。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="40&#32;实战：Redis&#32;集群模式（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="42&#32;技能学习指南.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a9c98e070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
