<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>34 实战：Redis 慢查询.md</title>
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

                    <a class="current-tab" href="34&#32;实战：Redis&#32;慢查询.md">34 实战：Redis 慢查询.md</a>
                    

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
                        <div><h1>34 实战：Redis 慢查询</h1>
<p>Redis 慢查询作用和 MySQL 慢查询作用类似，都是为我们查询出不合理的执行命令，然后让开发人员和运维人员一起来规避这些耗时的命令，从而让服务器更加高效和健康的运行。对于单线程的 Redis 来说，不合理的使用更是致命的，因此掌握 Redis 慢查询技能对我们来说非常的关键。</p>
<h3>如何进行慢查询？</h3>
<p>在开始之前，我们先要了解一下 Redis 中和慢查询相关的配置项，Redis 慢查询重要的配置项有以下两个：</p>
<ul>
<li>slowlog-log-slower-than：用于设置慢查询的评定时间，也就是说超过此配置项的命令，将会被当成慢操作记录在慢查询日志中，它执行单位是微秒（1 秒等于 1000000 微秒）；</li>
<li>slowlog-max-len：用来配置慢查询日志的最大记录数。</li>
</ul>
<p>我们先来看它们的默认配置值：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; config get slowlog-log-slower-than #慢查询判断时间
1) &quot;slowlog-log-slower-than&quot;
2) &quot;10000&quot;
127.0.0.1:6379&gt; config get slowlog-max-len #慢查询最大记录条数
1) &quot;slowlog-max-len&quot;
2) &quot;128&quot;

</code></pre>
<p>可以看出慢查询的临界值是 10000 微秒，默认保存 128 条慢查询记录。</p>
<h4><strong>修改配置项</strong></h4>
<p>slowlog-log-slower-than 和 slowlog-max-len 可以通过  <code>config set xxx</code> 的模式来修改，例如 <code>config set slowlog-max-len 200</code> 设置慢查询最大记录数为 200 条。</p>
<h4><strong>慢查询演示</strong></h4>
<p>我们先来设置慢查询的判断时间为 0 微秒，这样所有的执行命令都会被记录，设置命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; config set slowlog-log-slower-than 0
OK

</code></pre>
<p>接下来我们执行两条插入命令：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; set msg xiaoming
OK
127.0.0.1:6379&gt; set lang java
OK

</code></pre>
<p>最后我们使用 <code>slowlog show</code> 来查询慢日志，结果如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; slowlog get #慢日志查询
1) 1) (integer) 2 #慢日志下标
   2) (integer) 1581994139 #执行时间
   3) (integer) 5 #花费时间 (单位微秒)
   4) 1) &quot;set&quot; #执行的具体命令
      2) &quot;lang&quot;
      3) &quot;java&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;
2) 1) (integer) 1
   2) (integer) 1581994131
   3) (integer) 6
   4) 1) &quot;set&quot;
      2) &quot;msg&quot;
      3) &quot;xiaoming&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;
3) 1) (integer) 0
   2) (integer) 1581994093
   3) (integer) 5
   4) 1) &quot;config&quot;
      2) &quot;set&quot;
      3) &quot;slowlog-log-slower-than&quot;
      4) &quot;0&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;

</code></pre>
<p>加上本身的设置命令一共有三条“慢操作”记录，按照插入的顺序倒序存入慢查询日志中。</p>
<blockquote>
<p>小贴士：当慢查询日志超过设定的最大存储条数之后，会把最早的执行命令依次舍弃。</p>
</blockquote>
<h3>慢查询其他相关命令</h3>
<h4><strong>查询指定条数慢日志</strong></h4>
<p>语法：<code>slowlog get n</code>。</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; slowlog get 2 #查询两条
1) 1) (integer) 20
   2) (integer) 1581997567
   3) (integer) 14
   4) 1) &quot;slowlog&quot;
      2) &quot;get&quot;
      3) &quot;4&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;
2) 1) (integer) 19
   2) (integer) 1581997544
   3) (integer) 11
   4) 1) &quot;slowlog&quot;
      2) &quot;get&quot;
      3) &quot;3&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;
127.0.0.1:6379&gt; slowlog get 3 #查询三条
1) 1) (integer) 22
   2) (integer) 1581997649
   3) (integer) 25
   4) 1) &quot;set&quot;
      2) &quot;msg&quot;
      3) &quot;hi&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;
2) 1) (integer) 21
   2) (integer) 1581997613
   3) (integer) 9
   4) 1) &quot;slowlog&quot;
      2) &quot;get&quot;
      3) &quot;2&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;
3) 1) (integer) 20
   2) (integer) 1581997567
   3) (integer) 14
   4) 1) &quot;slowlog&quot;
      2) &quot;get&quot;
      3) &quot;4&quot;
   5) &quot;127.0.0.1:47068&quot;
   6) &quot;&quot;

</code></pre>
<h4><strong>获取慢查询队列长度</strong></h4>
<p>语法：<code>slowlog len</code>。</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; slowlog len
(integer) 16

</code></pre>
<h4><strong>清空慢查询日志</strong></h4>
<p>使用 <code>slowlog reset</code> 来清空所有的慢查询日志，执行命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; slowlog reset
OK

</code></pre>
<h3>代码实战</h3>
<p>本文我们使用 Java 来实现慢查询日志的操作，代码如下：</p>
<pre><code class="language-java">import redis.clients.jedis.Jedis;
import redis.clients.jedis.util.Slowlog;
import utils.JedisUtils;

import java.util.List;

/**
 * 慢查询
 */
public class SlowExample {
    public static void main(String[] args) {
        Jedis jedis = JedisUtils.getJedis();
        // 插入慢查询（因为 slowlog-log-slower-than 设置为 0，所有命令都符合慢操作）
        jedis.set(&quot;db&quot;, &quot;java&quot;);
        jedis.set(&quot;lang&quot;, &quot;java&quot;);
        // 慢查询记录的条数
        long logLen = jedis.slowlogLen();
        // 所有慢查询
        List&lt;Slowlog&gt; list = jedis.slowlogGet();
        // 循环打印
        for (Slowlog item : list) {
            System.out.println(&quot;慢查询命令：&quot;+ item.getArgs()+
                    &quot; 执行了：&quot;+item.getExecutionTime()+&quot; 微秒&quot;);
        }
        // 清空慢查询日志
        jedis.slowlogReset();
    }
}

</code></pre>
<p>以上代码执行结果如下：</p>
<pre><code>慢查询命令：[SLOWLOG, len] 执行了：1 微秒
慢查询命令：[SET, lang, java] 执行了：2 微秒
慢查询命令：[SET, db, java] 执行了：4 微秒

慢查询命令：[SLOWLOG, reset] 执行了：155 微秒

</code></pre>
<h3>小结</h3>
<p>本文我们介绍了慢查询相关的两个重要参数 slowlog-log-slower-than（用于设置慢查询的评定时间）和 slowlog-max-len 用来配置慢查询日志的最大记录数，然后通过修改 <code>config set slowlog-log-slower-than 0</code> 把所有操作都记录在慢日志进行相关测试。我们可以使用 <code>slowlog get [n]</code> 查询慢操作日志，使用 <code>slowlog reset</code> 清空慢查询日志。最后给大家一个建议，可以定期检查慢查询日志，及时发现和改进 Redis 运行中不合理的操作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="33&#32;实战：Redis&#32;性能测试.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="35&#32;实战：Redis&#32;性能优化方案.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a6d7be370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
