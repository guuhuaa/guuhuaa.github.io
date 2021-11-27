<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>26 消息队列终极解决方案——Stream（上）.md</title>
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

                    <a class="current-tab" href="26&#32;消息队列终极解决方案——Stream（上）.md">26 消息队列终极解决方案——Stream（上）.md</a>
                    

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
                        <div><h1>26 消息队列终极解决方案——Stream（上）</h1>
<p>在 Redis 5.0 Stream 没出来之前，消息队列的实现方式都有着各自的缺陷，例如：</p>
<ul>
<li>发布订阅模式 PubSub，不能持久化也就无法可靠的保存消息，并且对于离线重连的客户端不能读取历史消息的缺陷；</li>
<li>列表实现消息队列的方式不能重复消费，一个消息消费完就会被删除；</li>
<li>有序集合消息队列的实现方式不能存储相同 value 的消息，并且不能阻塞读取消息。</li>
</ul>
<p>并且以上三种方式在实现消息队列时，只能存储单 value 值，也就是如果你要存储一个对象的情况下，必须先序列化成 JSON 字符串，在读取之后还要反序列化成对象才行，这也给用户的使用带来的不便，基于以上问题，Redis 5.0 便推出了 Stream 类型也是此版本最重要的功能，用于完美地实现消息队列，它借鉴了 Kafka 的设计思路，它支持消息的持久化和消息轨迹的消费，支持 ack 确认消息的模式，让消息队列更加的稳定和可靠。</p>
<p>接下来我们先来了解 Stream 自身的一些特性，然后在综合 Stream 的特性，结合 Java 代码完整的实现一个完美的消息队列示例。</p>
<h3>基础使用</h3>
<p>Stream 既然是一个数据类型，那么和其他数据类型相似，它也有一些自己的操作方法，例如：</p>
<ul>
<li>xadd 添加消息；</li>
<li>xlen 查询消息长度；</li>
<li>xdel 根据消息 ID 删除消息；</li>
<li>del 删除整个 Stream；</li>
<li>xrange 读取区间消息</li>
<li>xread 读取某个消息之后的消息。</li>
</ul>
<p>具体使用如下所述。</p>
<h4><strong>添加消息</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xadd key * name redis age 10
&quot;1580880750844-0&quot; #结果返回的是消息 id

</code></pre>
<p>其中 <code>*</code> 表示使用 Redis 的规则：时间戳 + 序号的方式自动生成 ID，用户也可以自己指定 ID。</p>
<p>相关语法：</p>
<pre><code>xadd key ID field string [field string ...]

</code></pre>
<h4><strong>查询消息的长度</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xlen key
(integer) 1

</code></pre>
<p>相关语法：</p>
<pre><code>xlen key

</code></pre>
<h4><strong>删除消息</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xadd key * name redis
&quot;1580881585129-0&quot; #消息 ID
127.0.0.1:6379&gt; xlen key
(integer) 1
127.0.0.1:6379&gt; xdel key 1580881585129-0 #删除消息，根据 ID
(integer) 1
127.0.0.1:6379&gt; xlen key
(integer) 0

</code></pre>
<p>相关语法：</p>
<pre><code>xdel key ID [ID ...]

</code></pre>
<p>此命令支持删除一条或多条消息，根据消息 ID。</p>
<h4><strong>删除整个 Stream</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; del key #删除整个 Stream
(integer) 1
127.0.0.1:6379&gt; xlen key
(integer) 0

</code></pre>
<p>相关语法：</p>
<pre><code>del key [key ...]

</code></pre>
<p>此命令支持删除一个或多个 Stream。</p>
<h4><strong>查询区间消息</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xrange mq - +
1) 1) &quot;1580882060464-0&quot;
   2) 1) &quot;name&quot;
      2) &quot;redis&quot;
      3) &quot;age&quot;
      4) &quot;10&quot;
2) 1) &quot;1580882071524-0&quot;
   2) 1) &quot;name&quot;
      2) &quot;java&quot;
      3) &quot;age&quot;
      4) &quot;20&quot;

</code></pre>
<p>其中：<code>-</code> 表示第一条消息，<code>+</code> 表示最后一条消息。</p>
<p>相关语法：</p>
<pre><code>xrange key start end [COUNT count]

</code></pre>
<h4><strong>查询某个消息之后的消息</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xread count 1 streams mq 1580882060464-0
1) 1) &quot;mq&quot;
   2) 1) 1) &quot;1580882071524-0&quot;
         2) 1) &quot;name&quot;
            2) &quot;java&quot;
            3) &quot;age&quot;
            4) &quot;20&quot;

</code></pre>
<p>在名称为 mq 的 Stream 中，从消息 ID 为 1580882060464-0 的，往后查询一条消息。</p>
<p>相关语法：</p>
<pre><code>xread [COUNT count] [BLOCK milliseconds] STREAMS key [key ...] ID [ID ...]

</code></pre>
<p>此命令提供了阻塞读的参数 block，我们可以使用它读取从当前数据以后新增数据，命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xread count 1 block 0 streams mq $

</code></pre>
<p>其中 <code>block 0</code> 表示一直阻塞，<code>$</code> 表示从最后开始读取，这个时候新开一个命令行插入一条数据，此命令展示的结果如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xadd mq * name sql age 20 #新窗口添加数据
&quot;1580890737890-0&quot;
#阻塞读取到的新数据
127.0.0.1:6379&gt; xread count 1 block 0 streams mq $
1) 1) &quot;mq&quot;
   2) 1) 1) &quot;1580890737890-0&quot;
         2) 1) &quot;name&quot;
            2) &quot;sql&quot;
            3) &quot;age&quot;
            4) &quot;20&quot;
(36.37s)

</code></pre>
<h3>基础版消息队列</h3>
<p>使用 Stream 消费分组实现消息队列的功能和列表方式的消息队列比较相似，使用 xadd 命令和 xread 循环读取就可以实现基础版的消息队列，具体代码如下：</p>
<pre><code class="language-java">import com.google.gson.Gson;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.StreamEntry;
import redis.clients.jedis.StreamEntryID;
import java.util.AbstractMap;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StreamExample {
    public static void main(String[] args) throws InterruptedException {
        // 消费者
        new Thread(() -&gt; consumer()).start();
        Thread.sleep(1000);
        // 生产者
        producer();
    }
    /**
     * 生产者
     */
    public static void producer() throws InterruptedException {
        Jedis jedis = new Jedis(&quot;127.0.0.1&quot;, 6379);
        // 推送消息
        Map&lt;String, String&gt; map = new HashMap&lt;&gt;();
        map.put(&quot;name&quot;, &quot;redis&quot;);
        map.put(&quot;age&quot;, &quot;10&quot;);
        // 添加消息
        StreamEntryID id = jedis.xadd(&quot;mq&quot;, null, map);
        System.out.println(&quot;消息添加成功 ID：&quot; + id);
    }
    /**
     * 消费者
     */
    public static void consumer() {
        Jedis jedis = new Jedis(&quot;127.0.0.1&quot;, 6379);
        // 消费消息
        while (true) {
            // 获取消息，new StreamEntryID().LAST_ENTRY 标识获取当前时间以后的新增消息
            Map.Entry&lt;String, StreamEntryID&gt; entry = new AbstractMap.SimpleImmutableEntry&lt;&gt;(&quot;mq&quot;,
                    new StreamEntryID().LAST_ENTRY);
            // 阻塞读取一条消息（最大阻塞时间120s）
            List&lt;Map.Entry&lt;String, List&lt;StreamEntry&gt;&gt;&gt; list = jedis.xread(1, 120 * 1000, entry);
            if (list.size() == 1) {
                // 读取到消息
                System.out.println(&quot;读取到消息 ID：&quot; + list.get(0).getValue().get(0).getID());
                // 使用 Gson 来打印 JSON 格式的消息内容
                System.out.println(&quot;内容：&quot; + new Gson().toJson(list.get(0).getValue().get(0).getFields()));
            }
        }
    }
}

</code></pre>
<p>以上代码运行结果如下：</p>
<pre><code>消息添加成功 ID：1580895735148-0
读取到消息 ID：1580895735148-0
内容：{&quot;name&quot;:&quot;redis&quot;,&quot;age&quot;:&quot;10&quot;}

</code></pre>
<p>以上代码需要特殊说明的是，我们使用 <code>new StreamEntryID().LAST_ENTRY</code> 来实现读取当前时间以后新增的消息，如果要从头读取历史消息把这行代码中的 <code>.LAST_ENTRY</code> 去掉即可。</p>
<p>还有一点需要注意，在 Jedis 框架中如果使用 jedis.xread() 方法来阻塞读取消息队列，第二个参数 long block 必须设置大于 0，如果设置小于 0，此阻塞条件就无效了，我查看了 jedis 的源码发现，它只有判断在大于 0 的时候才会设置阻塞属性，源码如下：</p>
<pre><code class="language-java">if (block &gt; 0L) {
    params[streamsIndex++] = Keyword.BLOCK.raw;
    params[streamsIndex++] = Protocol.toByteArray(block);
}

</code></pre>
<p>所以 block 属性我们可以设置一个比较大的值来阻塞读取消息。</p>
<blockquote>
<p>所谓的阻塞读取消息指的是当队列中没有数据时会进入休眠模式，等有数据之后才会唤醒继续执行。</p>
</blockquote>
<h3>小结</h3>
<p>本文介绍了 Stream 的基础方法，并使用 xadd 存入消息和 xread 循环阻塞读取消息的方式实现了简易版的消息队列，交互流程如下图所示：</p>
<p><img src="assets/3e54f6b0-6f6f-11ea-832c-2703165cf4af" alt="Stream简易版交互图.png" /></p>
<p>然后这些并不是 Stream 最核心的功能，下文我们将带领读者朋友们，使用消费分组来实现一个完美的消息队列。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="25&#32;消息队列的其他实现方式.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="27&#32;消息队列终极解决方案——Stream（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a3b59b070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
