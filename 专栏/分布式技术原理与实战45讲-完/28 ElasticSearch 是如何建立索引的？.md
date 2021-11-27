<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>28 ElasticSearch 是如何建立索引的？.md</title>
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

                    
                    <a href="00&#32;开篇词：搭建分布式知识体系，挑战高薪&#32;Offer.md">00 开篇词：搭建分布式知识体系，挑战高薪 Offer.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;如何证明分布式系统的&#32;CAP&#32;理论？.md">01 如何证明分布式系统的 CAP 理论？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;不同数据一致性模型有哪些应用？.md">02 不同数据一致性模型有哪些应用？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;如何透彻理解&#32;Paxos&#32;算法？.md">03 如何透彻理解 Paxos 算法？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;ZooKeeper&#32;如何保证数据一致性？.md">04 ZooKeeper 如何保证数据一致性？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;共识问题：区块链如何确认记账权？.md">05 共识问题：区块链如何确认记账权？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;如何准备一线互联网公司面试？.md">06 如何准备一线互联网公司面试？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;分布式事务有哪些解决方案？.md">07 分布式事务有哪些解决方案？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;对比两阶段提交，三阶段协议有哪些改进？.md">08 对比两阶段提交，三阶段协议有哪些改进？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;MySQL&#32;数据库如何实现&#32;XA&#32;规范？.md">09 MySQL 数据库如何实现 XA 规范？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;如何在业务中体现&#32;TCC&#32;事务模型？.md">10 如何在业务中体现 TCC 事务模型？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;分布式锁有哪些应用场景和实现？.md">11 分布式锁有哪些应用场景和实现？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;如何使用&#32;Redis&#32;快速实现分布式锁？.md">12 如何使用 Redis 快速实现分布式锁？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/13%20%E5%88%86%E5%B8%83%E5%BC%8F%E4%BA%8B%E5%8A%A1%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">13 分布式事务考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;如何理解&#32;RPC&#32;远程服务调用？.md">14 如何理解 RPC 远程服务调用？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;为什么微服务需要&#32;API&#32;网关？.md">15 为什么微服务需要 API 网关？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;如何实现服务注册与发现？.md">16 如何实现服务注册与发现？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;如何实现分布式调用跟踪？.md">17 如何实现分布式调用跟踪？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;分布式下如何实现配置管理？.md">18 分布式下如何实现配置管理？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;容器化升级对服务有哪些影响？.md">19 容器化升级对服务有哪些影响？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;ServiceMesh：服务网格有哪些应用？.md">20 ServiceMesh：服务网格有哪些应用？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;Dubbo&#32;vs&#32;Spring&#32;Cloud：两大技术栈如何选型？.md">21 Dubbo vs Spring Cloud：两大技术栈如何选型？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/22%20%E5%88%86%E5%B8%83%E5%BC%8F%E6%9C%8D%E5%8A%A1%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">22 分布式服务考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;读写分离如何在业务中落地？.md">23 读写分离如何在业务中落地？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;为什么需要分库分表，如何实现？.md">24 为什么需要分库分表，如何实现？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;存储拆分后，如何解决唯一主键问题？.md">25 存储拆分后，如何解决唯一主键问题？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;分库分表以后，如何实现扩容？.md">26 分库分表以后，如何实现扩容？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;NoSQL&#32;数据库有哪些典型应用？.md">27 NoSQL 数据库有哪些典型应用？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="28&#32;ElasticSearch&#32;是如何建立索引的？.md">28 ElasticSearch 是如何建立索引的？.md</a>
                    

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/29%20%E5%88%86%E5%B8%83%E5%BC%8F%E5%AD%98%E5%82%A8%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">29 分布式存储考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;消息队列有哪些应用场景？.md">30 消息队列有哪些应用场景？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;集群消费和广播消费有什么区别？.md">31 集群消费和广播消费有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;业务上需要顺序消费，怎么保证时序性？.md">32 业务上需要顺序消费，怎么保证时序性？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;消息幂等：如何保证消息不被重复消费？.md">33 消息幂等：如何保证消息不被重复消费？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;高可用：如何实现消息队列的&#32;HA？.md">34 高可用：如何实现消息队列的 HA？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;消息队列选型：Kafka&#32;如何实现高性能？.md">35 消息队列选型：Kafka 如何实现高性能？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;消息队列选型：RocketMQ&#32;适用哪些场景？.md">36 消息队列选型：RocketMQ 适用哪些场景？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/37%20%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">37 消息队列考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;不止业务缓存，分布式系统中还有哪些缓存？.md">38 不止业务缓存，分布式系统中还有哪些缓存？.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;如何避免缓存穿透、缓存击穿、缓存雪崩？.md">39 如何避免缓存穿透、缓存击穿、缓存雪崩？.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;经典问题：先更新数据库，还是先更新缓存？.md">40 经典问题：先更新数据库，还是先更新缓存？.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;失效策略：缓存过期都有哪些策略？.md">41 失效策略：缓存过期都有哪些策略？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;负载均衡：一致性哈希解决了哪些问题？.md">42 负载均衡：一致性哈希解决了哪些问题？.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;缓存高可用：缓存如何保证高可用？.md">43 缓存高可用：缓存如何保证高可用？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/44%20%E5%88%86%E5%B8%83%E5%BC%8F%E7%BC%93%E5%AD%98%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">44 分布式缓存考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="45&#32;从双十一看高可用的保障方式.md">45 从双十一看高可用的保障方式.md</a>

                </li>
                <li>

                    
                    <a href="46&#32;高并发场景下如何实现系统限流？.md">46 高并发场景下如何实现系统限流？.md</a>

                </li>
                <li>

                    
                    <a href="47&#32;降级和熔断：如何增强服务稳定性？.md">47 降级和熔断：如何增强服务稳定性？.md</a>

                </li>
                <li>

                    
                    <a href="48&#32;如何选择适合业务的负载均衡策略？.md">48 如何选择适合业务的负载均衡策略？.md</a>

                </li>
                <li>

                    
                    <a href="49&#32;线上服务有哪些稳定性指标？.md">49 线上服务有哪些稳定性指标？.md</a>

                </li>
                <li>

                    
                    <a href="50&#32;分布式下有哪些好用的监控组件？.md">50 分布式下有哪些好用的监控组件？.md</a>

                </li>
                <li>

                    
                    <a href="51&#32;分布式下如何实现统一日志系统？.md">51 分布式下如何实现统一日志系统？.md</a>

                </li>
                <li>

                    
                    <a href="52&#32;分布式路漫漫，厚积薄发才是王道.md">52 分布式路漫漫，厚积薄发才是王道.md</a>

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
                        <div><h1>28 ElasticSearch 是如何建立索引的？</h1>
<p>前面讲到了 NoSQL 数据库的应用，在关系型数据库和 NoSQL 数据库之外，还有一类非常重要的存储中间件，那就是<strong>文件索引</strong>。当你在电商网站搜索商品，或者在搜索引擎搜索资料时，都离不开基于文件索引的各种检索框架的支持。</p>
<p>这一课时我们就一起来看下以 ElasticSearch 为代表的文件索引相关的知识。</p>
<h3>ElasticSearch 简介</h3>
<p>在讨论 ElasticSearch 之前，不得不提 Apache Lucene，因为 ElasticSearch 的广泛应用离不开 Lucene 的支持。</p>
<p>Lucene 是一个开源的全文检索引擎类库，支持各种分词以及搜索相关的实现，可以极大地简化搜索开发的成本，但 Lucene 只是一个工具包，在实际项目中进行二次开发，你需要非常熟悉 Lucene 的实现机制以及 API 应用，这样才能应用 Lucene 的各种特性。</p>
<p>现在有了 ElasticSearch，就可以直接使用基于 Lucene 的各种检索功能，ElasticSearch 是一个基于 Lucene 的分布式全文检索框架，在 Lucene 类库的基础上实现，可以避免直接基于 Lucene 开发，这一点和 Java 中 Netty 对 IO/NIO 的封装有些类似。</p>
<p>ElasticSearch 开放了一系列的 RESTful API，基于这些 API，可以快捷地实现各种搜索功能。另外一方面，除了搜索相关的功能，ElasticSearch 还对分布式场景下的应用有特别好的支持，包括良好的扩展性，可以扩展到上百台服务器的集群规模，以及近似实时分析的索引实现。这些特点，使得 ElasticSearch 在各类搜索场景、大数据分析等业务中广泛应用。</p>
<h4>ElasticSearch 应用</h4>
<p>ElasticSearch 对搜索的支持非常好，但是和 NoSQL 数据库一样，对事务、一致性等的支持较低。</p>
<p>下面是一个实际开发中，常见的数据库-索引-缓存系统架构图：</p>
<p><img src="assets/Ciqc1F7-68eAeYw2AAF83MZQ2m0681.png" alt="25.png" /></p>
<p>可以看到，ElasticSearch 一般是作为持久性数据库的辅助存储，是和 SQL &amp; NoSQL 数据库一起使用，对外提供索引查询功能。关系型数据库保证数据更新的准确性，在关系型数据库更新以后，通过 binlog 同步结合消息队列分发的方式，来更新文件索引，提供一致性保证。</p>
<h4>ELK stack</h4>
<p>ElasticSearch 是由 Elastic 公司创建的，除了 ElasticSearch，Elastic 公司还有另外两款产品，分别是 Logstash 及 Kibana 开源项目，这三个开源项目组合在一起称为 ELK stack。</p>
<p>在 ELK 技术栈中，ElasticSearch 用于数据分析和检索，Logstash 用于日志收集，Kibana 用于界面的展示，ELK 可以用于快速查询数据并可视化分析，在日志处理、大数据等领域有非常广泛的应用。我在一个项目中曾经基于 ELK 部署过日志收集和告警系统，ELK 的文档和各种问题手册非常全面，可以说是开箱即用。</p>
<h3>索引是如何建立的</h3>
<p>ElasticSearch 存储的单元是<strong>索引</strong>，这一点区别于很多关系型数据库和 NoSQL 数据库，比如关系型数据库是按照关系表的形式组织数据，大部分 NoSQL 数据库是 K-Value 的键值对方式。</p>
<p>ElasticSearch 存储的基本单元是索引，那么索引是如何创建的呢？</p>
<p>ElasticSearch 索引的实现基于 Lucene，使用倒排索引的结构，倒排索引的引入，使得 ElasticSearch 可以非常高效地实现各种文件索引。倒排索引不光是在 ElasticSearch 等组件中应用，它还是百度等搜索引擎实现的底层技术之一。在搜索引擎中，索引的建立需要经过网页爬取、信息采集、分词、索引创建的过程，不过在 ElasticSearch 内部存储的实现中，数据的写入可以对比搜索引擎对网页的抓取和信息采集的过程，只需要关注分词和索引的创建。</p>
<h4>分词和索引</h4>
<p>分词是在索引建立中特别重要的一个环节，分词的策略会直接影响索引结果。Lucene 提供了多种分词器，分词器是一个可插拔的组件，包括内置的标准分词器， 也可以引入对中文支持较好的 IKAnalyze 中文分词器等。</p>
<p>下面我们通过一个例子来了解分词的具体过程，假设我们在 ElasticSearch 中新增了两个文档，每个文档包含如下内容：</p>
<ul>
<li>文档1，Jerry and Tom are good friends.</li>
<li>文档2，Good friends should help each other.</li>
</ul>
<p>英文是有单词的，单词之间通过空格进行拆分，所以对英文的分词相对容易，比如上面的内容，可以直接对字符串按照空格拆分，得到分词后的数组。</p>
<blockquote>
<p>Jerry /   / and /   / Tom /   / are /   / good /   / friends / .
Good /   / friends /   / should /   / help /   / each /   / other / .</p>
</blockquote>
<p>如果是中文，除了标点符号以外，一个整句是没有分隔符的，处理起来就会复杂得多。一般来说，中文分词用得比较多的策略是基于字典的最长字符串匹配方式，这种策略可以覆盖大多数场景，不过还是有一小部分天然存在歧义的文档是无法处理的。比如「学生会组织各种活动」，按照最长串匹配的方式，可以切分成“学生会/组织各种活动”，但实际要表达的可能是“学生/会/组织各种活动”。</p>
<p>现在有一个很火热的学科叫作自然语言处理，研究的问题就包括如何消除语义分析中的各种歧义问题，感兴趣的同学可以去了解下。</p>
<h4>建立索引</h4>
<p>索引存储的结构是倒排索引，什么是倒排索引呢？倒排索引是相对于正排索引来说的，倒排索引描述了一个映射关系，包括文档中分词后的结果，以及分别包含这些单词的文档列表。</p>
<p>索引描述的其实就是关键词和文档的关系，正排索引就是“文档—关键词”的格式，倒排索引则相反，是“关键词—文档”的格式。可以看到，当需要使用关键词进行检索时，使用倒排索引才能实现快速检索的目的。</p>
<p>针对上面的分词示例，我们简单起见，统一为小写，把分词之后的单词组成一个不重复的分词列表，为了更好地进行查找，可以按照字典序排序。</p>
<blockquote>
<p>and,are,each,friends,good,help,jerry,other,should,tom</p>
</blockquote>
<p>比如，其中“friends”在文档 1 和文档 2 中都出现了，“Tom”和“Jerry”只在文档 1 中出现了 1 次，其他的单词也进行同样地处理，于是我们可以构建下面的倒排索引：</p>
<table>
<thead>
<tr>
<th>分词</th>
<th>文档列表</th>
</tr>
</thead>
<tbody>
<tr>
<td>...</td>
<td>...</td>
</tr>
<tr>
<td>friends</td>
<td>文档 1，文档 2</td>
</tr>
<tr>
<td>good</td>
<td>文档 1，文档 2</td>
</tr>
<tr>
<td>jerry</td>
<td>文档 1，</td>
</tr>
<tr>
<td>tom</td>
<td>文档 1</td>
</tr>
<tr>
<td>...</td>
<td>以下省略</td>
</tr>
</tbody>
</table>
<p>具体到数据结构的实现，可以通过实现一个字典树，也就是 Trie 树，对字典树进行扩展，额外存储对应的数据块地址，定位到具体的数据位置。</p>
<p><img src="assets/CgqCHl77Do-AXYgbAABfeRIU95w684.png" alt="3.png" /></p>
<h4>对比 B+ 树</h4>
<p>MySQL InnoDB 引擎的索引实现是基于 B+ 树，那么同样是索引，倒排索引和 B+ 树索引有哪些区别呢？</p>
<p>严格地说，这两类索引是不能在一起比较的，B+ 树描述的是索引的数据结构，而倒排索引是通过索引的组织形式来命名的。比如我们上面的例子中，倒排指的是关键词和文档列表的结构关系。</p>
<p>对于数据库来说，索引的作用是提高数据查询的性能，考虑到磁盘寻址的特性，选择了 B+ 树作为索引的实现结构，可以更好地实现通过主键以及通过区间范围查找的要求。</p>
<p>对于倒排索引，则是对应具体的应用场景，我们在搜索中是通过一些关键词，定位到具体的文档。所以倒排索引实现的是根据关键词，也就是分词的结果，去查找文档，或者不同的网页。</p>
<h3>总结</h3>
<p>这一课时介绍了 ElasticSearch 存储组件及其应用，日志分析的三大件之 ELK 技术栈，以及倒排索引是如何实现的。</p>
<p>虽然 ElasticSearch 技术可以实现高效的检索，但是也带来了相应的部署以及一致性维护成本，在一些小型项目中，还是会用数据库模糊匹配的方式实现关键词检索。你可以思考一下，在你负责的项目中，是如何实现关键词检索的？欢迎留言分享。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="27&#32;NoSQL&#32;数据库有哪些典型应用？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/29%20%E5%88%86%E5%B8%83%E5%BC%8F%E5%AD%98%E5%82%A8%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4350c3ef1a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
