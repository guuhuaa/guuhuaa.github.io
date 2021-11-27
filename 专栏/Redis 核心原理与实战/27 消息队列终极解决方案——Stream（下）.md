<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>27 消息队列终极解决方案——Stream（下）.md</title>
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

                    <a class="current-tab" href="27&#32;消息队列终极解决方案——Stream（下）.md">27 消息队列终极解决方案——Stream（下）.md</a>
                    

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
                        <div><h1>27 消息队列终极解决方案——Stream（下）</h1>
<p>在开始使用消息分组之前，我们必须手动创建分组才行，以下是几个和 Stream 分组有关的命令，我们先来学习一下它的使用。</p>
<h3>消息分组命令</h3>
<h4><strong>创建消费者群组</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xgroup create mq group1 0-0 
OK

</code></pre>
<p>相关语法：</p>
<pre><code>xgroup create stream-key group-key ID

</code></pre>
<p>其中：</p>
<ul>
<li>mq 为 Stream 的 key；</li>
<li>group1 为分组的名称；</li>
<li>0-0 表示从第一条消息开始读取。</li>
</ul>
<p>如果要从当前最后一条消息向后读取，使用 <code>$</code> 即可，命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xgroup create mq group2 $
OK

</code></pre>
<h4><strong>读取消息</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xreadgroup group group1 c1 count 1 streams mq &gt;
1) 1) &quot;mq&quot;
   2) 1) 1) &quot;1580959593553-0&quot;
         2) 1) &quot;name&quot;
            2) &quot;redis&quot;
            3) &quot;age&quot;
            4) &quot;10&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>xreadgroup group group-key consumer-key streams stream-key

</code></pre>
<p>其中：</p>
<ul>
<li><code>&gt;</code> 表示读取下一条消息；</li>
<li>group1 表示分组名称；</li>
<li>c1 表示 consumer（消费者）名称。</li>
</ul>
<p>xreadgroup 命令和 xread 使用类似，也可以设置阻塞读取，命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xreadgroup group group1 c2 streams mq &gt;
1) 1) &quot;mq&quot;
   2) 1) 1) &quot;1580959606181-0&quot;
         2) 1) &quot;name&quot;
            2) &quot;java&quot;
            3) &quot;age&quot;
            4) &quot;20&quot;
127.0.0.1:6379&gt; xreadgroup group group1 c2 streams mq &gt;
(nil) #队列中的消息已经被读取完
127.0.0.1:6379&gt; xreadgroup group group1 c1 count 1 block 0 streams mq &gt; #阻塞读取

</code></pre>
<p>此时打开另一个命令行创建使用 xadd 添加一条消息，阻塞命令执行结果如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xreadgroup group group1 c1 count 1 block 0 streams mq &gt;
1) 1) &quot;mq&quot;
   2) 1) 1) &quot;1580961475368-0&quot;
         2) 1) &quot;name&quot;
            2) &quot;sql&quot;
            3) &quot;age&quot;
            4) &quot;20&quot;
(86.14s)

</code></pre>
<h4><strong>消息消费确认</strong></h4>
<p>接收到消息之后，我们要手动确认一下（ack），命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xack mq group1 1580959593553-0
(integer) 1

</code></pre>
<p>相关语法：</p>
<pre><code>xack key group-key ID [ID ...]

</code></pre>
<p>消费确认增加了消息的可靠性，一般在业务处理完成之后，需要执行 ack 确认消息已经被消费完成，整个流程的执行如下图所示：</p>
<p><img src="assets/a5dfbd80-6f72-11ea-833b-93fabc8068c9" alt="image.png" /></p>
<h4><strong>查询未确认的消费队列</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xpending mq group1
1) (integer) 1 #未确认（ack）的消息数量为 1 条
2) &quot;1580994063971-0&quot;
3) &quot;1580994063971-0&quot;
4) 1) 1) &quot;c1&quot;
      2) &quot;1&quot;
127.0.0.1:6379&gt; xack  mq group1 1580994063971-0 #消费确认
(integer) 1
127.0.0.1:6379&gt; xpending mq group1
1) (integer) 0 #没有未确认的消息
2) (nil)
3) (nil)
4) (nil)

</code></pre>
<h4><strong>xinfo 查询相关命令</strong></h4>
<p><strong>1. 查询流信息</strong></p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xinfo stream mq
 1) &quot;length&quot;
 2) (integer) 2 #队列中有两个消息
 3) &quot;radix-tree-keys&quot;
 4) (integer) 1
 5) &quot;radix-tree-nodes&quot;
 6) (integer) 2
 7) &quot;groups&quot;
 8) (integer) 1 #一个消费分组
 9) &quot;last-generated-id&quot;
10) &quot;1580959606181-0&quot;
11) &quot;first-entry&quot;
12) 1) &quot;1580959593553-0&quot;
    2) 1) &quot;name&quot;
       2) &quot;redis&quot;
       3) &quot;age&quot;
       4) &quot;10&quot;
13) &quot;last-entry&quot;
14) 1) &quot;1580959606181-0&quot;
    2) 1) &quot;name&quot;
       2) &quot;java&quot;
       3) &quot;age&quot;
       4) &quot;20&quot;

</code></pre>
<p>相关语法：</p>
<pre><code>xinfo stream stream-key

</code></pre>
<p><strong>2. 查询消费组消息</strong></p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xinfo groups mq
1) 1) &quot;name&quot;
   2) &quot;group1&quot; #消息分组名称
   3) &quot;consumers&quot;
   4) (integer) 1 #一个消费者客户端
   5) &quot;pending&quot;
   6) (integer) 1 #一个未确认消息
   7) &quot;last-delivered-id&quot;
   8) &quot;1580959593553-0&quot; #读取的最后一条消息 ID

</code></pre>
<p>相关语法：</p>
<pre><code>xinfo groups stream-key

</code></pre>
<p><strong>3. 查看消费者组成员信息</strong></p>
<pre><code class="language-shell">127.0.0.1:6379&gt; xinfo consumers mq group1
1) 1) &quot;name&quot;
   2) &quot;c1&quot; #消费者名称
   3) &quot;pending&quot;
   4) (integer) 0 #未确认消息
   5) &quot;idle&quot;
   6) (integer) 481855

</code></pre>
<p>相关语法：</p>
<pre><code>xinfo consumers stream group-key

</code></pre>
<h4><strong>删除消费者</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xgroup delconsumer mq group1 c1
(integer) 1

</code></pre>
<p>相关语法：</p>
<pre><code>xgroup delconsumer stream-key group-key consumer-key

</code></pre>
<h4><strong>删除消费组</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; xgroup destroy mq group1
(integer) 1

</code></pre>
<p>相关语法：</p>
<pre><code>xgroup destroy stream-key group-key

</code></pre>
<h3>代码实战</h3>
<p>接下来我们使用 Jedis 来实现 Stream 分组消息队列，代码如下：</p>
<pre><code class="language-java">import com.google.gson.Gson;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.StreamEntry;
import redis.clients.jedis.StreamEntryID;
import utils.JedisUtils;

import java.util.AbstractMap;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StreamGroupExample {
    private static final String _STREAM_KEY = &quot;mq&quot;; // 流 key
    private static final String _GROUP_NAME = &quot;g1&quot;; // 分组名称
    private static final String _CONSUMER_NAME = &quot;c1&quot;; // 消费者 1 的名称
    private static final String _CONSUMER2_NAME = &quot;c2&quot;; // 消费者 2 的名称
    public static void main(String[] args) {
        // 生产者
        producer();
        // 创建消费组
        createGroup(_STREAM_KEY, _GROUP_NAME);
        // 消费者 1
        new Thread(() -&gt; consumer()).start();
        // 消费者 2
        new Thread(() -&gt; consumer2()).start();
    }
    /**
     * 创建消费分组
     * @param stream    流 key
     * @param groupName 分组名称
     */
    public static void createGroup(String stream, String groupName) {
        Jedis jedis = JedisUtils.getJedis();
        jedis.xgroupCreate(stream, groupName, new StreamEntryID(), true);
    }
    /**
     * 生产者
     */
    public static void producer() {
        Jedis jedis = JedisUtils.getJedis();
        // 添加消息 1
        Map&lt;String, String&gt; map = new HashMap&lt;&gt;();
        map.put(&quot;data&quot;, &quot;redis&quot;);
        StreamEntryID id = jedis.xadd(_STREAM_KEY, null, map);
        System.out.println(&quot;消息添加成功 ID：&quot; + id);
        // 添加消息 2
        Map&lt;String, String&gt; map2 = new HashMap&lt;&gt;();
        map2.put(&quot;data&quot;, &quot;java&quot;);
        StreamEntryID id2 = jedis.xadd(_STREAM_KEY, null, map2);
        System.out.println(&quot;消息添加成功 ID：&quot; + id2);
    }
    /**
     * 消费者 1
     */
    public static void consumer() {
        Jedis jedis = JedisUtils.getJedis();
        // 消费消息
        while (true) {
            // 读取消息
            Map.Entry&lt;String, StreamEntryID&gt; entry = new AbstractMap.SimpleImmutableEntry&lt;&gt;(_STREAM_KEY,
                    new StreamEntryID().UNRECEIVED_ENTRY);
            // 阻塞读取一条消息（最大阻塞时间120s）
            List&lt;Map.Entry&lt;String, List&lt;StreamEntry&gt;&gt;&gt; list = jedis.xreadGroup(_GROUP_NAME, _CONSUMER_NAME, 1,
                    120 * 1000, true, entry);
            if (list != null &amp;&amp; list.size() == 1) {
                // 读取到消息
                Map&lt;String, String&gt; content = list.get(0).getValue().get(0).getFields(); // 消息内容
                System.out.println(&quot;Consumer 1 读取到消息 ID：&quot; + list.get(0).getValue().get(0).getID() +
                        &quot; 内容：&quot; + new Gson().toJson(content));
            }
        }
    }
    /**
     * 消费者 2
     */
    public static void consumer2() {
        Jedis jedis = JedisUtils.getJedis();
        // 消费消息
        while (true) {
            // 读取消息
            Map.Entry&lt;String, StreamEntryID&gt; entry = new AbstractMap.SimpleImmutableEntry&lt;&gt;(_STREAM_KEY,
                    new StreamEntryID().UNRECEIVED_ENTRY);
            // 阻塞读取一条消息（最大阻塞时间120s）
            List&lt;Map.Entry&lt;String, List&lt;StreamEntry&gt;&gt;&gt; list = jedis.xreadGroup(_GROUP_NAME, _CONSUMER2_NAME, 1,
                    120 * 1000, true, entry);
            if (list != null &amp;&amp; list.size() == 1) {
                // 读取到消息
                Map&lt;String, String&gt; content = list.get(0).getValue().get(0).getFields(); // 消息内容
                System.out.println(&quot;Consumer 2 读取到消息 ID：&quot; + list.get(0).getValue().get(0).getID() +
                        &quot; 内容：&quot; + new Gson().toJson(content));
            }
        }
    }
}

</code></pre>
<p>以上代码运行结果如下：</p>
<pre><code>消息添加成功 ID：1580971482344-0
消息添加成功 ID：1580971482415-0
Consumer 1 读取到消息 ID：1580971482344-0 内容：{&quot;data&quot;:&quot;redis&quot;}
Consumer 2 读取到消息 ID：1580971482415-0 内容：{&quot;data&quot;:&quot;java&quot;}

</code></pre>
<p>其中，jedis.xreadGroup() 方法的第五个参数 noAck 表示是否自动确认消息，如果设置 true 收到消息会自动确认（ack）消息，否则则需要手动确认。</p>
<blockquote>
<p>注意：Jedis 框架要使用最新版，低版本 block 设置大于 0 时，会有 bug 抛连接超时异常。</p>
</blockquote>
<p>可以看出，同一个分组内的多个 consumer 会读取到不同消息，不同的 consumer 不会读取到分组内的同一条消息。</p>
<h3>小结</h3>
<p>本文我们介绍了 Stream 分组的相关知识，使用 Jedis 的 xreadGroup() 方法实现了消息的阻塞读取，并且使用此方法自带 noAck 参数，实现了消息的自动确认，通过本文我们也知道了，一个分组内的多个 consumer 会轮询收到消息队列的消息，并且不会出现一个消息被多个 consumer 读取的情况。</p>
<p>如果你看了本文的知识还是觉得没看懂，那是因为你没有结合实践去理解，所以如果对本文还有疑问，跟着本文一步一步实践起来吧。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="26&#32;消息队列终极解决方案——Stream（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="28&#32;实战：分布式锁详解与代码.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a404dc270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
