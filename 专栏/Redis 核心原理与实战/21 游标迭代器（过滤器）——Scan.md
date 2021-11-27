<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>21 游标迭代器（过滤器）——Scan.md</title>
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

                    <a class="current-tab" href="21&#32;游标迭代器（过滤器）——Scan.md">21 游标迭代器（过滤器）——Scan.md</a>
                    

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
                        <div><h1>21 游标迭代器（过滤器）——Scan</h1>
<h3>一个问题引发的「血案」</h3>
<p>曾经发生过这样一件事，我们的 Redis 服务器存储了海量的数据，其中登录用户信息是以 user_token_id 的形式存储的。运营人员想要当前所有的用户登录信息，然后悲剧就发生了：因为我们的工程师使用了 <code>keys user_token_*</code> 来查询对应的用户，结果导致 Redis 假死不可用，以至于影响到线上的其他业务接连发生问题，然后就收到了一堆的系统预警短信。并且这个假死的时间是和存储的数据成正比的，数据量越大假死的时间就越长，导致的故障时间也越长。</p>
<p>那如何避免这个问题呢？</p>
<h3>问题的解决方案</h3>
<p>在 Redis 2.8 之前，我们只能使用 keys 命令来查询我们想要的数据，但这个命令存在两个缺点：</p>
<ol>
<li>此命令没有分页功能，我们只能一次性查询出所有符合条件的 key 值，如果查询结果非常巨大，那么得到的输出信息也会非常多；</li>
<li>keys 命令是遍历查询，因此它的查询时间复杂度是 o(n)，所以数据量越大查询时间就越长。</li>
</ol>
<p>然而，比较幸运的是在 Redis 2.8 时推出了 Scan，解决了我们这些问题，下面来看 Scan 的具体使用。</p>
<h3>Scan 命令使用</h3>
<p>我们先来模拟海量数据，使用 Pipeline 添加 10w 条数据，Java 代码实现如下：</p>
<pre><code class="language-java">import redis.clients.jedis.Jedis;
import redis.clients.jedis.Pipeline;
import utils.JedisUtils;

public class ScanExample {
    public static void main(String[] args) {
        // 添加 10w 条数据
        initData();
    }
    public static void initData(){
        Jedis jedis = JedisUtils.getJedis();
        Pipeline pipe = jedis.pipelined();
        for (int i = 1; i &lt; 100001; i++) {
            pipe.set(&quot;user_token_&quot; + i, &quot;id&quot; + i);
        }
        // 执行命令
        pipe.sync();
        System.out.println(&quot;数据插入完成&quot;);
    }
}

</code></pre>
<p>我们来查询用户 id 为 9999* 的数据，Scan 命令使用如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; scan 0 match user_token_9999* count 10000
1) &quot;127064&quot;
2) 1) &quot;user_token_99997&quot;
127.0.0.1:6379&gt; scan 127064 match user_token_9999* count 10000
1) &quot;1740&quot;
2) 1) &quot;user_token_9999&quot;
127.0.0.1:6379&gt; scan 1740 match user_token_9999* count 10000
1) &quot;21298&quot;
2) 1) &quot;user_token_99996&quot;
127.0.0.1:6379&gt; scan 21298 match user_token_9999* count 10000
1) &quot;65382&quot;
2) (empty list or set)
127.0.0.1:6379&gt; scan 65382 match user_token_9999* count 10000
1) &quot;78081&quot;
2) 1) &quot;user_token_99998&quot;
   2) &quot;user_token_99992&quot;
127.0.0.1:6379&gt; scan 78081 match user_token_9999* count 10000
1) &quot;3993&quot;
2) 1) &quot;user_token_99994&quot;
   2) &quot;user_token_99993&quot;
127.0.0.1:6379&gt; scan 3993 match user_token_9999* count 10000
1) &quot;13773&quot;
2) 1) &quot;user_token_99995&quot;
127.0.0.1:6379&gt; scan 13773 match user_token_9999* count 10000
1) &quot;47923&quot;
2) (empty list or set)
127.0.0.1:6379&gt; scan 47923 match user_token_9999* count 10000
1) &quot;59751&quot;
2) 1) &quot;user_token_99990&quot;
   2) &quot;user_token_99991&quot;
   3) &quot;user_token_99999&quot;
127.0.0.1:6379&gt; scan 59751 match user_token_9999* count 10000
1) &quot;0&quot;
2) (empty list or set)

</code></pre>
<p>从以上的执行结果，我们看出两个问题：</p>
<ol>
<li>查询的结果为空，但游标值不为 0，表示遍历还没结束；</li>
<li>设置的是 count 10000，但每次返回的数量都不是 10000，且不固定，这是因为 count 只是限定服务器单次遍历的字典槽位数量（约等于），而不是规定返回结果的 count 值。</li>
</ol>
<p>相关语法：</p>
<pre><code>scan cursor [MATCH pattern] [COUNT count]

</code></pre>
<p>其中：</p>
<ul>
<li>cursor：光标位置，整数值，从 0 开始，到 0 结束，查询结果是空，但游标值不为 0，表示遍历还没结束；</li>
<li>match pattern：正则匹配字段；</li>
<li>count：限定服务器单次遍历的字典槽位数量（约等于），只是对增量式迭代命令的一种提示（hint），并不是查询结果返回的最大数量，它的默认值是 10。</li>
</ul>
<h3>代码实战</h3>
<p>本文我们使用 Java 代码来实现 Scan 的查询功能，代码如下：</p>
<pre><code class="language-java">import redis.clients.jedis.Jedis;
import redis.clients.jedis.Pipeline;
import redis.clients.jedis.ScanParams;
import redis.clients.jedis.ScanResult;
import utils.JedisUtils;

public class ScanExample {
    public static void main(String[] args) {
        Jedis jedis = JedisUtils.getJedis();
        // 定义 match 和 count 参数
        ScanParams params = new ScanParams();
        params.count(10000);
        params.match(&quot;user_token_9999*&quot;);
        // 游标
        String cursor = &quot;0&quot;;
        while (true) {
            ScanResult&lt;String&gt; res = jedis.scan(cursor, params);
            if (res.getCursor().equals(&quot;0&quot;)) {
                // 表示最后一条
                break;
            }
            cursor = res.getCursor(); // 设置游标
            for (String item : res.getResult()) {
                // 打印查询结果
                System.out.println(&quot;查询结果：&quot; + item);
            }
        }
    }
}

</code></pre>
<p>以上程序执行结果如下：</p>
<pre><code>查询结果：user_token_99997
查询结果：user_token_9999
查询结果：user_token_99996
查询结果：user_token_99998
查询结果：user_token_99992
查询结果：user_token_99994
查询结果：user_token_99993
查询结果：user_token_99995
查询结果：user_token_99990
查询结果：user_token_99991
查询结果：user_token_99999

</code></pre>
<h3>Scan 相关命令</h3>
<p>Scan 是一个系列指令，除了 Scan 之外，还有以下 3 个命令：</p>
<ol>
<li>HScan 遍历字典游标迭代器</li>
<li>SScan 遍历集合的游标迭代器</li>
<li>ZScan 遍历有序集合的游标迭代器</li>
</ol>
<p>来看这些命令的具体使用。</p>
<h4><strong>HScan 使用</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; hscan myhash 0 match k2* count 10
1) &quot;0&quot;
2) 1) &quot;k2&quot;
   2) &quot;v2&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>hscan key cursor [MATCH pattern] [COUNT count]

</code></pre>
<h4><strong>SScan 使用</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; sscan myset 0 match v2* count 20
1) &quot;0&quot;
2) 1) &quot;v2&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>sscan key cursor [MATCH pattern] [COUNT count]

</code></pre>
<h4><strong>ZScan 使用</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; zscan zset 0 match red* count 20
1) &quot;0&quot;
2) 1) &quot;redis&quot;
   2) &quot;10&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>zscan key cursor [MATCH pattern] [COUNT count]

</code></pre>
<h3>Scan 说明</h3>
<p>官方对 Scan 命令的描述信息如下。</p>
<h4><strong>Scan guarantees</strong></h4>
<blockquote>
<p>The SCAN command, and the other commands in the SCAN family, are able to provide to the user a set of guarantees associated to full iterations.</p>
<ul>
<li>A full iteration always retrieves all the elements that were present in the collection from the start to the end of a full iteration. This means that if a given element is inside the collection when an iteration is started, and is still there when an iteration terminates, then at some point SCANreturned it to the user.</li>
<li>A full iteration never returns any element that was NOT present in the collection from the start to the end of a full iteration. So if an element was removed before the start of an iteration, and is never added back to the collection for all the time an iteration lasts, SCAN ensures that this element will never be returned.</li>
</ul>
<p>However because SCAN has very little state associated (just the cursor) it has the following drawbacks:</p>
<ul>
<li>A given element may be returned multiple times. It is up to the application to handle the case of duplicated elements, for example only using the returned elements in order to perform operations that are safe when re-applied multiple times.</li>
<li>Elements that were not constantly present in the collection during a full iteration, may be returned or not: it is undefined.</li>
</ul>
</blockquote>
<p>官方文档地址：</p>
<blockquote>
<p><a href="https://redis.io/commands/scan">https://redis.io/commands/scan</a></p>
</blockquote>
<p>翻译为中文的含义是：Scan 及它的相关命令可以保证以下查询规则。</p>
<ul>
<li>它可以完整返回开始到结束检索集合中出现的所有元素，也就是在整个查询过程中如果这些元素没有被删除，且符合检索条件，则一定会被查询出来；</li>
<li>它可以保证不会查询出，在开始检索之前删除的那些元素。</li>
</ul>
<p>然后，Scan 命令包含以下缺点：</p>
<ul>
<li>一个元素可能被返回多次，需要客户端来实现去重；</li>
<li>在迭代过程中如果有元素被修改，那么修改的元素能不能被遍历到不确定。</li>
</ul>
<h3>小结</h3>
<p>通过本文我们可以知道 Scan 包含以下四个指令：</p>
<ol>
<li>Scan：用于检索当前数据库中所有数据；</li>
<li>HScan：用于检索哈希类型的数据；</li>
<li>SScan：用于检索集合类型中的数据；</li>
<li>ZScan：由于检索有序集合中的数据。</li>
</ol>
<p>Scan 具备以下几个特点：</p>
<ol>
<li>Scan 可以实现 keys 的匹配功能；</li>
<li>Scan 是通过游标进行查询的不会导致 Redis 假死；</li>
<li>Scan 提供了 count 参数，可以规定遍历的数量；</li>
<li>Scan 会把游标返回给客户端，用户客户端继续遍历查询；</li>
<li>Scan 返回的结果可能会有重复数据，需要客户端去重；</li>
<li>单次返回空值且游标不为 0，说明遍历还没结束；</li>
<li>Scan 可以保证在开始检索之前，被删除的元素一定不会被查询出来；</li>
<li>在迭代过程中如果有元素被修改， Scan 不保证能查询出相关的元素。</li>
</ol>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="20&#32;查询附近的人——GEO.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="22&#32;优秀的基数统计算法——HyperLogLog.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a1ebd6a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
