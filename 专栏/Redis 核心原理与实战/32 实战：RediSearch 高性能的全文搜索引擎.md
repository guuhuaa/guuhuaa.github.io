<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>32 实战：RediSearch 高性能的全文搜索引擎.md</title>
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

                    <a class="current-tab" href="32&#32;实战：RediSearch&#32;高性能的全文搜索引擎.md">32 实战：RediSearch 高性能的全文搜索引擎.md</a>
                    

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
                        <div><h1>32 实战：RediSearch 高性能的全文搜索引擎</h1>
<p>RediSearch 是一个高性能的全文搜索引擎，它可以作为一个 Redis Module（扩展模块）运行在 Redis 服务器上。</p>
<p>RediSearch 主要特性如下：</p>
<ul>
<li>基于文档的多个字段全文索引</li>
<li>高性能增量索引</li>
<li>文档排序（由用户在索引时手动提供）</li>
<li>在子查询之间使用 AND 或 NOT 操作符的复杂布尔查询</li>
<li>可选的查询子句</li>
<li>基于前缀的搜索</li>
<li>支持字段权重设置</li>
<li>自动完成建议（带有模糊前缀建议）</li>
<li>精确的短语搜索</li>
<li>在许多语言中基于词干分析的查询扩展</li>
<li>支持用于查询扩展和评分的自定义函数</li>
<li>将搜索限制到特定的文档字段</li>
<li>数字过滤器和范围</li>
<li>使用 Redis 自己的地理命令进行地理过滤</li>
<li>Unicode 支持（需要 UTF-8 字符集）</li>
<li>检索完整的文档内容或只是 ID 的检索</li>
<li>支持文档删除和更新与索引垃圾收集</li>
<li>支持部分更新和条件文档更新</li>
</ul>
<h3>安装</h3>
<p>和前面讲到布隆过滤器的引入方式一样，我们可以使用 RediSearch 官方推荐的 Docker 方式来安装并启动 RediSearch 功能，操作命令如下：</p>
<pre><code>docker run -p 6379:6379 redislabs/redisearch:latest

</code></pre>
<p>安装并启动成功，如下图所示：</p>
<p><img src="assets/29f9b8e0-7b3b-11ea-8940-6df1558f5aa2" alt="RediSearch安装成功.png" /></p>
<p>安装完成之后<strong>使用 redis-cli 来检查 RediSearch 模块是否加载成功</strong>，使用 Docker 启动 redis-cli，命令如下：</p>
<pre><code>docker exec -it myredis redis-cli

</code></pre>
<p>其中“myredis”为 Redis 服务器的名称，执行结果如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; module list
1) 1) &quot;name&quot;
   2) &quot;ft&quot;
   3) &quot;ver&quot;
   4) (integer) 10610

</code></pre>
<p>返回数组存在“ft”，表明 RediSearch 模块已经成功加载。</p>
<h4><strong>源码方式安装</strong></h4>
<p>如果不想使用 Docker，我们也可以使用源码的方式进行安装，安装命令如下：</p>
<pre><code class="language-shell">git clone https://github.com/RedisLabsModules/RediSearch.git
cd RediSearch # 进入模块目录
make all

</code></pre>
<p>安装完成之后，可以使用如下命令启动 Redis 并加载 RediSearch 模块，命令如下：</p>
<pre><code class="language-shell">src/redis-server redis.conf --loadmodule ../RediSearch/src/redisearch.so

</code></pre>
<h3>使用</h3>
<p>我们先使用 redis-cli 来对 RediSearch 进行相关的操作。</p>
<h4><strong>创建索引和字段</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.create myidx schema title text weight 5.0 desc text
OK

</code></pre>
<p>其中“myidx”为索引的ID，此索引包含了两个字段“title”和“desc”，“weight”为权重，默认值为 1.0。</p>
<h4><strong>将内容添加到索引</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.add myidx doc1 1.0 fields title &quot;He urged her to study English&quot; desc &quot;good idea&quot;
OK

</code></pre>
<p>其中“doc1”为文档 ID（docid），“1.0”为评分（score）。</p>
<h4><strong>根据关键查询</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.search myidx &quot;english&quot; limit 0 10
1) (integer) 1
2) &quot;doc1&quot;
3) 1) &quot;title&quot;
   2) &quot;He urged her to study English&quot;
   3) &quot;desc&quot;
   4) &quot;good idea&quot;

</code></pre>
<p>可以看出我们使用 title 字段中的关键字“english”查询出了一条满足查询条件的数据。</p>
<h4><strong>中文搜索</strong></h4>
<p>首先我们需要先给索引中，添加一条中文数据，执行命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.add myidx doc2 1.0 language &quot;chinese&quot; fields title &quot;Java 14 发布了！新功能速览&quot; desc &quot;Java 14 在 2020.3.17 日发布正式版了，但现在很多公司还在使用 Java 7 或 Java 8&quot;
OK

</code></pre>
<p>注意：<strong>这里必须要设置语言编码为中文，也就是“language &quot;chinese&quot;”</strong>，默认是英文编码，如果不设置则无法支持中文查询（无法查出结果）。</p>
<p>我们使用之前的查询方式，命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.search myidx &quot;正式版&quot;
1) (integer) 0

</code></pre>
<p>我们发现并没有查到任何信息，这是因为我们没有指定搜索的语言，不但保存时候要指定编码，查询时也需要指定，查询命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.search myidx &quot;发布了&quot; language &quot;chinese&quot;
1) (integer) 1
2) &quot;doc2&quot;
3) 1) &quot;desc&quot;
   2) &quot;Java 14 \xe5\x9c\xa8 2020.3.17 \xe6\x97\xa5\xe5\x8f\x91\xe5\xb8\x83\xe6\xad\xa3\xe5\xbc\x8f\xe7\x89\x88\xe4\xba\x86\xef\xbc\x8c\xe4\xbd\x86\xe7\x8e\xb0\xe5\x9c\xa8\xe5\xbe\x88\xe5\xa4\x9a\xe5\x85\xac\xe5\x8f\xb8\xe8\xbf\x98\xe5\x9c\xa8\xe4\xbd\xbf\xe7\x94\xa8 Java 7 \xe6\x88\x96 Java 8&quot;
   3) &quot;title&quot;
   4) &quot;Java 14 \xe5\x8f\x91\xe5\xb8\x83\xe4\xba\x86\xef\xbc\x81\xe6\x96\xb0\xe5\x8a\x9f\xe8\x83\xbd\xe9\x80\x9f\xe8\xa7\x88&quot;

</code></pre>
<p>从结果可以看出中文信息已经被顺利的查询出来了。</p>
<h4><strong>删除索引的数据</strong></h4>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.del myidx doc1
(integer) 1

</code></pre>
<p>我们使用索引加文档 ID 就可以实现删除数据的功能。</p>
<h4><strong>删除索引</strong></h4>
<p>我们可以使用“ft.drop”关键字删除整个索引，执行命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.drop myidx
OK

</code></pre>
<h4><strong>查询索引详细信息</strong></h4>
<p>我们可以使用“ft.info”关键查询索引相关信息，执行命令如下：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; ft.info myidx
 1) index_name
 2) myidx
 3) index_options
 4) (empty list or set)
 5) fields
 6) 1) 1) title
       2) type
       3) TEXT
       4) WEIGHT
       5) &quot;5&quot;
    2) 1) desc
       2) type
       3) TEXT
       4) WEIGHT
       5) &quot;1&quot;
 7) num_docs
 8) &quot;2&quot;
 9) max_doc_id
10) &quot;2&quot;
11) num_terms
12) &quot;9&quot;
13) num_records
14) &quot;18&quot;
15) inverted_sz_mb
16) &quot;0.000102996826171875&quot;
17) total_inverted_index_blocks
18) &quot;29&quot;
19) offset_vectors_sz_mb
20) &quot;1.71661376953125e-05&quot;
21) doc_table_size_mb
22) &quot;0.000164031982421875&quot;
23) sortable_values_size_mb
24) &quot;0&quot;
25) key_table_size_mb
26) &quot;8.0108642578125e-05&quot;
27) records_per_doc_avg
28) &quot;9&quot;
29) bytes_per_record_avg
30) &quot;6&quot;
31) offsets_per_term_avg
32) &quot;1&quot;
33) offset_bits_per_record_avg
34) &quot;8&quot;
35) gc_stats
36)  1) bytes_collected
     2) &quot;0&quot;
     3) total_ms_run
     4) &quot;16&quot;
     5) total_cycles
     6) &quot;14&quot;
     7) avarage_cycle_time_ms
     8) &quot;1.1428571428571428&quot;
     9) last_run_time_ms
    10) &quot;2&quot;
    11) gc_numeric_trees_missed
    12) &quot;0&quot;
    13) gc_blocks_denied
    14) &quot;0&quot;
37) cursor_stats
38) 1) global_idle
    2) (integer) 0
    3) global_total
    4) (integer) 0
    5) index_capacity
    6) (integer) 128
    7) index_total
    8) (integer) 0

</code></pre>
<p>其中“num_docs”表示存储的数据数量。</p>
<h3>代码实战</h3>
<p>RediSearch 支持的客户端有以下这些。</p>
<p><img src="assets/4fb832a0-7b3b-11ea-b348-9df247d9e896" alt="image.png" /></p>
<p>本文我们使用 JRediSearch 来实现全文搜索的功能，首先在 pom.xml 添加 JRediSearch 引用：</p>
<pre><code class="language-xml">&lt;!-- https://mvnrepository.com/artifact/com.redislabs/jredisearch --&gt;
&lt;dependency&gt;
  &lt;groupId&gt;com.redislabs&lt;/groupId&gt;
  &lt;artifactId&gt;jredisearch&lt;/artifactId&gt;
  &lt;version&gt;1.3.0&lt;/version&gt;
&lt;/dependency&gt;

</code></pre>
<p>完整的操作代码如下：</p>
<pre><code class="language-shell">import io.redisearch.client.AddOptions;
import io.redisearch.client.Client;
import io.redisearch.Document;
import io.redisearch.SearchResult;
import io.redisearch.Query;
import io.redisearch.Schema;

public class RediSearchExample {
    public static void main(String[] args) {
        // 连接 Redis 服务器和指定索引
        Client client = new Client(&quot;myidx&quot;, &quot;127.0.0.1&quot;, 6379);
        // 定义索引
        Schema schema = new Schema().addTextField(&quot;title&quot;,
                5.0).addTextField(&quot;desc&quot;, 1.0);
        // 删除索引
        client.dropIndex();
        // 创建索引
        client.createIndex(schema, Client.IndexOptions.Default());
        // 设置中文编码
        AddOptions addOptions = new AddOptions();
        addOptions.setLanguage(&quot;chinese&quot;);
        // 添加数据
        Document document = new Document(&quot;doc1&quot;);
        document.set(&quot;title&quot;, &quot;天气预报&quot;);
        document.set(&quot;desc&quot;, &quot;今天的天气很好，是个阳光明媚的大晴天，有蓝蓝的天空和白白的云朵。&quot;);
        // 向索引中添加文档
        client.addDocument(document,addOptions);
        // 查询
        Query q = new Query(&quot;天气&quot;) // 设置查询条件
                .setLanguage(&quot;chinese&quot;) // 设置为中文编码
                .limit(0,5);
        // 返回查询结果
        SearchResult res = client.search(q);
        // 输出查询结果
        System.out.println(res.docs);
    }
}

</code></pre>
<p>以上程序执行结果如下：</p>
<pre><code>[{&quot;id&quot;:&quot;doc1&quot;,&quot;score&quot;:1.0,&quot;properties&quot;:{&quot;title&quot;:&quot;天气预报&quot;,&quot;desc&quot;:&quot;今天的天气很好，是个阳光明媚的大晴天，有蓝蓝的天空和白白的云朵。&quot;}}]

</code></pre>
<p>可以看出添加的中文数据，被正确的查询出来了。</p>
<h3>小结</h3>
<p>本文我们使用 Docker 和 源码编译的方式成功的启动了 RediSearch 功能，要使用 RediSearch 的全文搜索功能，必须先要创建一个索引，然后再索引中添加数据，再使用 ft.search 命令进行全文搜索，如果要查询中文内容的话，需要在添加数据时设置中文编码，并且在查询时也要设置中文编码，指定“language &quot;chinese&quot;”。</p>
<p><strong>参考 &amp; 鸣谢</strong></p>
<p>官网地址：</p>
<blockquote>
<p><a href="http://redisearch.io/">http://redisearch.io</a></p>
</blockquote>
<p>项目地址：</p>
<blockquote>
<p><a href="https://github.com/RediSearch/RediSearch">https://github.com/RediSearch/RediSearch</a></p>
</blockquote>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="31&#32;实战：定时任务案例.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="33&#32;实战：Redis&#32;性能测试.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a5faa8470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
