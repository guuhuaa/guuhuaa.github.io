<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>27 NoSQL 数据库有哪些典型应用？.md</title>
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

                    <a class="current-tab" href="27&#32;NoSQL&#32;数据库有哪些典型应用？.md">27 NoSQL 数据库有哪些典型应用？.md</a>
                    

                </li>
                <li>

                    
                    <a href="28&#32;ElasticSearch&#32;是如何建立索引的？.md">28 ElasticSearch 是如何建立索引的？.md</a>

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
                        <div><h1>27 NoSQL 数据库有哪些典型应用？</h1>
<p>前面的内容介绍了数据库读写分离和分库分表相关知识，都是针对关系型数据库的，即通常说的 RDBMS。除了关系型数据库，NoSQL 在项目开发中也有着越来越重要的作用，与此同时，NoSQL 相关的内容也是面试的常客。今天我们一起来看下 NoSQL 数据库有哪些应用。</p>
<h3>对比关系型数据库</h3>
<p>在介绍 NoSQL 数据库之前，先回顾下关系型数据库。还记得 SQL 语言的全称吗？Structured Query Language，也就是结构化查询语言，结构化查询对应的存储实现是关系型数据库，我们熟悉的 MySQL、Oracle 和 SQL Server，都是关系型数据库的代表。</p>
<p>关系型数据库通过关系模型来组织数据，在关系型数据库当中一个表就是一个模型，一个关系数据库可以包含多个表，不同数据表之间的联系反映了关系约束。</p>
<p>不知道你是否应用过 ER 图？在早期的软件工程中，数据表的创建都会通过 ER 图来定义，ER 图（Entity Relationship Diagram）称为<strong>实体-联系图</strong>，包括实体、属性和关系三个核心部分。</p>
<p>下面是在电商领域中，一个简化的会员、商品和订单的 ER 图：</p>
<p><img src="assets/Ciqc1F70ch6AfLu7AADzJKnY7FI638.png" alt="24.png" />
简化版的会员、商品和订单 ER 图</p>
<p>ER图中的实体采用矩形表示，即数据模型中的数据对象，例如电商业务模型中的会员、商品、订单等，每个数据对象具有不同的属性，比如会员有账户名、电话、地址等，商品有商品名称、价格、库存等属性。不同的数据对象之间又对应不同的关系，比如会员购买商品、创建订单。</p>
<p>有了 ER 图等的辅助设计，关系型数据库的数据模型可以非常好的描述物理世界，比较方便地创建各种数据约束。</p>
<p>另外一方面，关系型数据库对事务支持较好，支持 SQL 规范中的各种复杂查询，比如 join、union 等操作。正是由于对 SQL 规范的支持，也使得关系型数据库对扩展不友好，比较难进行分布式下的集群部署。</p>
<h3>NoSQL 数据库特性</h3>
<p>NoSQL 数据库是在 SQL 的基础上发展的，对 NoSQL 的具体解释，你可以认为是 Not Only SQL，也可以认为是 Non-Relational SQL。</p>
<p>NoSQL 对应非关系型数据库，不同于传统的关系型数据库，如果说关系型数据库是武侠小说中的正统功夫，NoSQL 数据库就是野路子，少了很多约束，也就不拘一格、自成一派。那么对比关系型数据库，NoSQL 型数据库有哪些优点呢？</p>
<ul>
<li><strong>良好的扩展性，容易通过集群部署</strong></li>
</ul>
<p>关系型数据库在进行扩展时，要考虑到如何分库分表、扩容等，各种实现方案都比较重，对业务侵入较大。NoSQL 数据库去掉了关系型数据库的关系特性，天生对集群友好，这样就非常容易扩展。</p>
<ul>
<li><strong>读写性能高，支持大数据量</strong></li>
</ul>
<p>关系型数据库对一致性的要求较高，数据表的结构复杂，读写的性能要低于非关系型数据库。另外一方面，部分 NoSQL 数据库采用全内存实现，更适合一些高并发的访问场景。</p>
<ul>
<li><strong>不限制表结构，灵活的数据模型</strong></li>
</ul>
<p>应用关系型数据库，需要通过 DML 语句创建表结构，数据表创建以后，增删字段需要重新修改表结构。如果使用 NoSQL，一般不需要事先为数据建立存储结构和字段，可以存储各种自定义的数据。</p>
<p>NoSQL 数据库有这么多优点，但是在项目开发中，关系型数据库和非关系型数据库不是对立的，而是相辅相成的。从性能的角度来讲，NoSQL 数据库的性能优于关系型数据库，从持久化角度，关系型数据库优于 NoSQL 数据库。</p>
<p>专栏最开始提到了 CAP 理论，从 CAP 的角度，NoSQL 数据库一般提供弱一致性的保证，实现最终一致性，也就是关系型数据库强调 CP 模型，而 NoSQL 关注的是 AP 模型，同时应用 NoSQL 和关系型数据库，可以满足高性能的基础上，同时保证数据可靠性。</p>
<h3>NoSQL 数据库应用</h3>
<p>非关系型数据库有很多类型，应用的侧重点也不同，可以从以下几个角度进行分类。</p>
<h4>Key-Value 数据库</h4>
<p>Key-Value 存储就是我们熟悉的 Map 结构，支持高性能的通过 Key 定位和存储。通常用来实现缓存等应用，典型的有 Redis 和 Memcached。</p>
<p>以 Redis 为例，作为应用最多的非关系型数据库之一，Redis 可以说是日常工作中的一把瑞士军刀。</p>
<p>从性能的角度，为了提高读写效率，Redis 在最开始的版本中一直使用单线程模型，避免上下文切换和线程竞争资源，并且采用了 IO 多路复用的技术，提升了性能，另外在最近的版本更新中，Redis也开始支持多线程处理，感兴趣的同学可以查看相关的资料了解。</p>
<p>从存储结构的角度，Redis 支持多种数据结构，得益于这些，Redis 有丰富的应用场景，并且针对不同的数据规模等，Redis 采取多种内存优化方式，尽量减少内存占用。比如，List 结构内部有压缩列表和双向链表两种实现，在数据规模较小时采用 ZipList 实现，特别是在新的版本更新中，又添加了 QuickList 的实现，减少内存的消耗。</p>
<p>从高可用的角度，作为一个内存数据库，Redis实现了AOF和RDB的数据持久化机制，另外，Redis支持了多种集群方式，包括主从同步，Sentinel和Redis Cluster等机制，提高了整体的数据安全和高可用保障。</p>
<h4>文档型数据库</h4>
<p>文档型数据库可以存储结构化的文档，比如 JSON 或者 XML，从这个角度上看，文档型数据库比较接近关系型数据库。但是对比关系型数据库，文档性数据库中不需要预先定义表结构，并且可以支持文档之间的嵌套，典型的比如 MongoDB，这一点和关系型数据库有很大的不同。</p>
<p>以 MongoDB 为例，采用了基于 JSON 扩展的 BSON 存储结构，可以进行自我描述，这种灵活的文档类型，特别适合应用在内容管理系统等业务中。MongoDB 还具备非常优秀的扩展能力，对分片等集群部署的支持非常全面，可以快速扩展集群规模。</p>
<h4>列存储数据库</h4>
<p>列式数据库被用来存储海量数据，比如 Cassandra、HBase 等，特点是大数据量下读写速度较快、可扩展性强，更容易进行分布式部署。</p>
<p>以 HBase 为例，HBase 支持海量数据的读写，特别是写入操作，可以支持 TB 级的数据量。列式数据库通常不支持事务和各种索引优化，比如 HBase 使用 LSM 树组织数据，对比 MySQL 的 B+ 树，在高并发写入时有更好的性能。</p>
<h4>图形数据库</h4>
<p>在一些特定的应用场景可以应用特殊的数据库，比如图形数据库。在学习数据结构时我们知道，社交网络中的用户关系可以使用图来存储，于是诞生了一些图形数据库，可以方便地操作图结构的相关算法，比如最短路径、关系查找等。</p>
<p>图形数据库在一般的工程开发中应用较少，感兴趣的同学可以去了解一下。</p>
<h3>总结</h3>
<p>这一课时分享了 NoSQL 数据库相关的知识点，包括关系型数据库和非关系型数据库的对比，分析了常见 NoSQL 数据库的分类和应用特性。</p>
<p>大多数场景下，NoSQL 数据库是配合关系型数据库一起使用的，这就涉及了不同存储之间的同步问题，比如缓存和数据库的同步等，针对这个问题，会在缓存模块展开介绍。现在你可以结合自己的项目实践，思考下应用过哪些非关系型数据库，以及使用了哪些对应特性，如何配合关系型数据库等，欢迎留言分享。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="26&#32;分库分表以后，如何实现扩容？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="28&#32;ElasticSearch&#32;是如何建立索引的？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4350bf1a9b645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
