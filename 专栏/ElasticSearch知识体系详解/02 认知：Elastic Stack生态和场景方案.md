<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 认知：Elastic Stack生态和场景方案.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>02 认知：Elastic Stack生态和场景方案</h1>
<h2>Elastic Stack生态</h2>
<blockquote>
<p>Beats + Logstash + ElasticSearch + Kibana</p>
</blockquote>
<p>如下是我从官方博客中找到图，这张图展示了ELK生态以及基于ELK的场景（最上方）</p>
<p><img src="assets/es-introduce-1-1.png" alt="img" /></p>
<p>由于Elastic X-Pack是面向收费的，所以我们不妨也把X-Pack放进去，看看哪些是由X-Pack带来的，在阅读官网文档时将方便你甄别重点：</p>
<p><img src="assets/es-introduce-1-0.png" alt="img" /></p>
<h3>Beats</h3>
<p>Beats是一个面向<strong>轻量型采集器</strong>的平台，这些采集器可以从边缘机器向Logstash、ElasticSearch发送数据，它是由Go语言进行开发的，运行效率方面比较快。从下图中可以看出，不同Beats的套件是针对不同的数据源。</p>
<p><img src="assets/es-introduce-2-0.png" alt="img" /></p>
<h3>Logstash</h3>
<p>Logstash是<strong>动态数据收集管道</strong>，拥有可扩展的插件生态系统，支持从不同来源采集数据，转换数据，并将数据发送到不同的存储库中。其能够与ElasticSearch产生强大的协同作用，后被Elastic公司在2013年收购。</p>
<p>它具有如下特性：</p>
<p>1）实时解析和转换数据；</p>
<p>2）可扩展，具有200多个插件；</p>
<p>3）可靠性、安全性。Logstash会通过持久化队列来保证至少将运行中的事件送达一次，同时将数据进行传输加密；</p>
<p>4）监控；</p>
<h3>ElasticSearch</h3>
<p>ElasticSearch对数据进行<strong>搜索、分析和存储</strong>，其是基于JSON的分布式搜索和分析引擎，专门为实现水平可扩展性、高可靠性和管理便捷性而设计的。</p>
<p>它的实现原理主要分为以下几个步骤：</p>
<p>1）首先用户将数据提交到ElasticSearch数据库中；</p>
<p>2）再通过分词控制器将对应的语句分词；</p>
<p>3）将分词结果及其权重一并存入，以备用户在搜索数据时，根据权重将结果排名和打分，将返回结果呈现给用户；</p>
<h3>Kibana</h3>
<p>Kibana实现<strong>数据可视化</strong>，其作用就是在ElasticSearch中进行民航。Kibana能够以图表的形式呈现数据，并且具有可扩展的用户界面，可以全方位的配置和管理ElasticSearch。</p>
<p>Kibana最早的时候是基于Logstash创建的工具，后被Elastic公司在2013年收购。</p>
<p>1）Kibana可以提供各种可视化的图表；</p>
<p>2）可以通过机器学习的技术，对异常情况进行检测，用于提前发现可疑问题；</p>
<h2>从日志收集系统看ES Stack的发展</h2>
<blockquote>
<p>我们看下ELK技术栈的演化，通常体现在日志收集系统中。</p>
</blockquote>
<p>一个典型的日志系统包括：</p>
<p>（1）收集：能够采集多种来源的日志数据</p>
<p>（2）传输：能够稳定的把日志数据解析过滤并传输到存储系统</p>
<p>（3）存储：存储日志数据</p>
<p>（4）分析：支持 UI 分析</p>
<p>（5）警告：能够提供错误报告，监控机制</p>
<h3>beats+elasticsearch+kibana</h3>
<p>Beats采集数据后，存储在ES中，有Kibana可视化的展示。</p>
<p><img src="assets/es-introduce-2-1.png" alt="img" /></p>
<h3>beats+logstath+elasticsearch+kibana</h3>
<p><img src="assets/es-introduce-2-2.png" alt="img" /></p>
<p>该框架是在上面的框架的基础上引入了logstash，引入logstash带来的好处如下：</p>
<p>（1）Logstash具有基于磁盘的自适应缓冲系统，该系统将吸收传入的吞吐量，从而减轻背压。</p>
<p>（2）从其他数据源（例如数据库，S3或消息传递队列）中提取。</p>
<p>（3）将数据发送到多个目的地，例如S3，HDFS或写入文件。</p>
<p>（4）使用条件数据流逻辑组成更复杂的处理管道。</p>
<p><strong>beats结合logstash带来的优势</strong>：</p>
<p>（1）水平可扩展性，高可用性和可变负载处理：beats和logstash可以实现节点之间的负载均衡，多个logstash可以实现logstash的高可用</p>
<p>（2）消息持久性与至少一次交付保证：使用beats或Winlogbeat进行日志收集时，可以保证至少一次交付。从Filebeat或Winlogbeat到Logstash以及从Logstash到Elasticsearch的两种通信协议都是同步的，并且支持确认。Logstash持久队列提供跨节点故障的保护。对于Logstash中的磁盘级弹性，确保磁盘冗余非常重要。</p>
<p>（3）具有身份验证和有线加密的端到端安全传输：从Beats到Logstash以及从 Logstash到Elasticsearch的传输都可以使用加密方式传递 。与Elasticsearch进行通讯时，有很多安全选项，包括基本身份验证，TLS，PKI，LDAP，AD和其他自定义领域</p>
<p><strong>增加更多的数据源</strong> 比如：TCP，UDP和HTTP协议是将数据输入Logstash的常用方法</p>
<p><img src="assets/es-introduce-2-3.png" alt="img" /></p>
<h3>beats+MQ+logstash+elasticsearch+kibana</h3>
<p><img src="assets/es-introduce-2-4.png" alt="img" /></p>
<p>在如上的基础上我们可以在beats和logstash中间添加一些组件redis、kafka、RabbitMQ等，添加中间件将会有如下好处：</p>
<p>（1）降低对日志所在机器的影响，这些机器上一般都部署着反向代理或应用服务，本身负载就很重了，所以尽可能的在这些机器上少做事；</p>
<p>（2）如果有很多台机器需要做日志收集，那么让每台机器都向Elasticsearch持续写入数据，必然会对Elasticsearch造成压力，因此需要对数据进行缓冲，同时，这样的缓冲也可以一定程度的保护数据不丢失；</p>
<p>（3）将日志数据的格式化与处理放到Indexer中统一做，可以在一处修改代码、部署，避免需要到多台机器上去修改配置；</p>
<h2>Elastic Stack最佳实践</h2>
<blockquote>
<p>我们再看下官方开发成员分享的最佳实践。</p>
</blockquote>
<h3>日志收集系统</h3>
<p>（PS：就是我们上面阐述的）</p>
<p>基本的日志系统</p>
<p><img src="assets/es-introduce-2-5.png" alt="img" /></p>
<p>增加数据源，和使用MQ</p>
<p><img src="assets/es-introduce-2-6.png" alt="img" /></p>
<h3>Metric收集和APM性能监控</h3>
<p><img src="assets/es-introduce-2-7.png" alt="img" /></p>
<h3>多数据中心方案</h3>
<p>通过冗余实现数据高可用</p>
<p><img src="assets/es-introduce-2-8.png" alt="img" /></p>
<p>两个数据采集中心（比如采集两个工厂的数据），采集数据后的汇聚</p>
<p><img src="assets/es-introduce-2-9.png" alt="img" /></p>
<p>数据分散，跨集群的搜索</p>
<p><img src="assets/es-introduce-2-10.png" alt="img" /></p>
<h2>参考文章</h2>
<ul>
<li>https://www.elastic.co/cn/elasticsearch/</li>
<li>https://www.elastic.co/pdf/architecture-best-practices.pdf</li>
<li>https://www.elastic.co/guide/en/logstash/current/deploying-and-scaling.html</li>
<li>https://www.cnblogs.com/supersnowyao/p/11110703.html</li>
<li>https://blog.51cto.com/wutengfei/2645627</li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;认知：ElasticSearch基础概念.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;安装：ElasticSearch和Kibana安装.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4340098d1470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
