<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL 故障诊断：一个 ALTER TALBE 执行了很久，你慌不慌？.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../index.html">
                <img src="../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="AQS&#32;万字图文全面解析.md">AQS 万字图文全面解析.md</a>

                </li>
                <li>

                    
                    <a href="Docker&#32;镜像构建原理及源码分析.md">Docker 镜像构建原理及源码分析.md</a>

                </li>
                <li>

                    
                    <a href="ElasticSearch&#32;小白从入门到精通.md">ElasticSearch 小白从入门到精通.md</a>

                </li>
                <li>

                    
                    <a href="JVM&#32;CPU&#32;Profiler技术原理及源码深度解析.md">JVM CPU Profiler技术原理及源码深度解析.md</a>

                </li>
                <li>

                    
                    <a href="JVM&#32;垃圾收集器.md">JVM 垃圾收集器.md</a>

                </li>
                <li>

                    
                    <a href="JVM&#32;面试的&#32;30&#32;个知识点.md">JVM 面试的 30 个知识点.md</a>

                </li>
                <li>

                    
                    <a href="Java&#32;IO&#32;体系、线程模型大总结.md">Java IO 体系、线程模型大总结.md</a>

                </li>
                <li>

                    
                    <a href="Java&#32;面试题集锦（网络篇）.md">Java 面试题集锦（网络篇）.md</a>

                </li>
                <li>

                    
                    <a href="Java-直接内存&#32;DirectMemory&#32;详解.md">Java-直接内存 DirectMemory 详解.md</a>

                </li>
                <li>

                    
                    <a href="Java中的SPI.md">Java中的SPI.md</a>

                </li>
                <li>

                    
                    <a href="Java中的ThreadLocal.md">Java中的ThreadLocal.md</a>

                </li>
                <li>

                    
                    <a href="Java线程池实现原理及其在美团业务中的实践.md">Java线程池实现原理及其在美团业务中的实践.md</a>

                </li>
                <li>

                    
                    <a href="Java魔法类：Unsafe应用解析.md">Java魔法类：Unsafe应用解析.md</a>

                </li>
                <li>

                    
                    <a href="Kafka&#32;源码阅读笔记.md">Kafka 源码阅读笔记.md</a>

                </li>
                <li>

                    
                    <a href="Kafka、ActiveMQ、RabbitMQ、RocketMQ&#32;区别以及高可用原理.md">Kafka、ActiveMQ、RabbitMQ、RocketMQ 区别以及高可用原理.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;Buffer&#32;Pool.md">MySQL · 引擎特性 · InnoDB Buffer Pool.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;IO子系统.md">MySQL · 引擎特性 · InnoDB IO子系统.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;事务系统.md">MySQL · 引擎特性 · InnoDB 事务系统.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;同步机制.md">MySQL · 引擎特性 · InnoDB 同步机制.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;数据页解析.md">MySQL · 引擎特性 · InnoDB 数据页解析.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB崩溃恢复.md">MySQL · 引擎特性 · InnoDB崩溃恢复.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;临时表那些事儿.md">MySQL · 引擎特性 · 临时表那些事儿.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;主从复制&#32;半同步复制.md">MySQL 主从复制 半同步复制.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;主从复制&#32;基于GTID复制.md">MySQL 主从复制 基于GTID复制.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;主从复制.md">MySQL 主从复制.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;事务日志(redo&#32;log和undo&#32;log).md">MySQL 事务日志(redo log和undo log).md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;亿级别数据迁移实战代码分享.md">MySQL 亿级别数据迁移实战代码分享.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;从一条数据说起-InnoDB行存储数据结构.md">MySQL 从一条数据说起-InnoDB行存储数据结构.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;地基基础：事务和锁的面纱.md">MySQL 地基基础：事务和锁的面纱.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;地基基础：数据字典.md">MySQL 地基基础：数据字典.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;地基基础：数据库字符集.md">MySQL 地基基础：数据库字符集.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;性能优化：碎片整理.md">MySQL 性能优化：碎片整理.md</a>

                </li>
                <li>

                    <a class="current-tab" href="MySQL&#32;故障诊断：一个&#32;ALTER&#32;TALBE&#32;执行了很久，你慌不慌？.md">MySQL 故障诊断：一个 ALTER TALBE 执行了很久，你慌不慌？.md</a>
                    

                </li>
                <li>

                    
                    <a href="MySQL&#32;故障诊断：如何在日志中轻松定位大事务.md">MySQL 故障诊断：如何在日志中轻松定位大事务.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;故障诊断：教你快速定位加锁的&#32;SQL.md">MySQL 故障诊断：教你快速定位加锁的 SQL.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;日志详解.md">MySQL 日志详解.md</a>

                </li>
                <li>

                    
                    <a href="MySQL&#32;的半同步是什么？.md">MySQL 的半同步是什么？.md</a>

                </li>
                <li>

                    
                    <a href="MySQL中的事务和MVCC.md">MySQL中的事务和MVCC.md</a>

                </li>
                <li>

                    
                    <a href="MySQL事务_事务隔离级别详解.md">MySQL事务_事务隔离级别详解.md</a>

                </li>
                <li>

                    
                    <a href="MySQL优化：优化&#32;select&#32;count().md">MySQL优化：优化 select count().md</a>

                </li>
                <li>

                    
                    <a href="MySQL共享锁、排他锁、悲观锁、乐观锁.md">MySQL共享锁、排他锁、悲观锁、乐观锁.md</a>

                </li>
                <li>

                    
                    <a href="MySQL的MVCC（多版本并发控制）.md">MySQL的MVCC（多版本并发控制）.md</a>

                </li>
                <li>

                    
                    <a href="QingStor&#32;对象存储架构设计及最佳实践.md">QingStor 对象存储架构设计及最佳实践.md</a>

                </li>
                <li>

                    
                    <a href="RocketMQ&#32;面试题集锦.md">RocketMQ 面试题集锦.md</a>

                </li>
                <li>

                    
                    <a href="SnowFlake&#32;雪花算法生成分布式&#32;ID.md">SnowFlake 雪花算法生成分布式 ID.md</a>

                </li>
                <li>

                    
                    <a href="Spring&#32;Boot&#32;2.x&#32;结合&#32;k8s&#32;实现分布式微服务架构.md">Spring Boot 2.x 结合 k8s 实现分布式微服务架构.md</a>

                </li>
                <li>

                    
                    <a href="Spring&#32;Boot&#32;教程：如何开发一个&#32;starter.md">Spring Boot 教程：如何开发一个 starter.md</a>

                </li>
                <li>

                    
                    <a href="Spring&#32;MVC&#32;原理.md">Spring MVC 原理.md</a>

                </li>
                <li>

                    
                    <a href="Spring&#32;MyBatis和Spring整合的奥秘.md">Spring MyBatis和Spring整合的奥秘.md</a>

                </li>
                <li>

                    
                    <a href="Spring&#32;帮助你更好的理解Spring循环依赖.md">Spring 帮助你更好的理解Spring循环依赖.md</a>

                </li>
                <li>

                    
                    <a href="Spring&#32;循环依赖及解决方式.md">Spring 循环依赖及解决方式.md</a>

                </li>
                <li>

                    
                    <a href="Spring中眼花缭乱的BeanDefinition.md">Spring中眼花缭乱的BeanDefinition.md</a>

                </li>
                <li>

                    
                    <a href="Vert.x&#32;基础入门.md">Vert.x 基础入门.md</a>

                </li>
                <li>

                    
                    <a href="eBay&#32;的&#32;Elasticsearch&#32;性能调优实践.md">eBay 的 Elasticsearch 性能调优实践.md</a>

                </li>
                <li>

                    
                    <a href="不可不说的Java“锁”事.md">不可不说的Java“锁”事.md</a>

                </li>
                <li>

                    
                    <a href="互联网并发限流实战.md">互联网并发限流实战.md</a>

                </li>
                <li>

                    
                    <a href="从ReentrantLock的实现看AQS的原理及应用.md">从ReentrantLock的实现看AQS的原理及应用.md</a>

                </li>
                <li>

                    
                    <a href="从SpringCloud开始，聊微服务架构.md">从SpringCloud开始，聊微服务架构.md</a>

                </li>
                <li>

                    
                    <a href="全面了解&#32;JDK&#32;线程池实现原理.md">全面了解 JDK 线程池实现原理.md</a>

                </li>
                <li>

                    
                    <a href="分布式一致性理论与算法.md">分布式一致性理论与算法.md</a>

                </li>
                <li>

                    
                    <a href="分布式一致性算法&#32;Raft.md">分布式一致性算法 Raft.md</a>

                </li>
                <li>

                    
                    <a href="分布式唯一&#32;ID&#32;解析.md">分布式唯一 ID 解析.md</a>

                </li>
                <li>

                    
                    <a href="分布式链路追踪：集群管理设计.md">分布式链路追踪：集群管理设计.md</a>

                </li>
                <li>

                    
                    <a href="动态代理种类及原理，你知道多少？.md">动态代理种类及原理，你知道多少？.md</a>

                </li>
                <li>

                    
                    <a href="响应式架构与&#32;RxJava&#32;在有赞零售的实践.md">响应式架构与 RxJava 在有赞零售的实践.md</a>

                </li>
                <li>

                    
                    <a href="大数据算法——布隆过滤器.md">大数据算法——布隆过滤器.md</a>

                </li>
                <li>

                    
                    <a href="如何设计一个亿级消息量的&#32;IM&#32;系统.md">如何设计一个亿级消息量的 IM 系统.md</a>

                </li>
                <li>

                    
                    <a href="异步网络模型.md">异步网络模型.md</a>

                </li>
                <li>

                    
                    <a href="当我们在讨论CQRS时，我们在讨论些神马？.md">当我们在讨论CQRS时，我们在讨论些神马？.md</a>

                </li>
                <li>

                    
                    <a href="彻底理解&#32;MySQL&#32;的索引机制.md">彻底理解 MySQL 的索引机制.md</a>

                </li>
                <li>

                    
                    <a href="最全的&#32;116&#32;道&#32;Redis&#32;面试题解答.md">最全的 116 道 Redis 面试题解答.md</a>

                </li>
                <li>

                    
                    <a href="有赞权限系统(SAM).md">有赞权限系统(SAM).md</a>

                </li>
                <li>

                    
                    <a href="有赞零售中台建设方法的探索与实践.md">有赞零售中台建设方法的探索与实践.md</a>

                </li>
                <li>

                    
                    <a href="服务注册与发现原理剖析（Eureka、Zookeeper、Nacos）.md">服务注册与发现原理剖析（Eureka、Zookeeper、Nacos）.md</a>

                </li>
                <li>

                    
                    <a href="深入浅出Cache.md">深入浅出Cache.md</a>

                </li>
                <li>

                    
                    <a href="深入理解&#32;MySQL&#32;底层实现.md">深入理解 MySQL 底层实现.md</a>

                </li>
                <li>

                    
                    <a href="漫画讲解&#32;git&#32;rebase&#32;VS&#32;git&#32;merge.md">漫画讲解 git rebase VS git merge.md</a>

                </li>
                <li>

                    
                    <a href="生成浏览器唯一稳定&#32;ID&#32;的探索.md">生成浏览器唯一稳定 ID 的探索.md</a>

                </li>
                <li>

                    
                    <a href="缓存&#32;如何保证缓存与数据库的双写一致性？.md">缓存 如何保证缓存与数据库的双写一致性？.md</a>

                </li>
                <li>

                    
                    <a href="网易严选怎么做全链路监控的？.md">网易严选怎么做全链路监控的？.md</a>

                </li>
                <li>

                    
                    <a href="美团万亿级&#32;KV&#32;存储架构与实践.md">美团万亿级 KV 存储架构与实践.md</a>

                </li>
                <li>

                    
                    <a href="美团点评Kubernetes集群管理实践.md">美团点评Kubernetes集群管理实践.md</a>

                </li>
                <li>

                    
                    <a href="解读《阿里巴巴&#32;Java&#32;开发手册》背后的思考.md">解读《阿里巴巴 Java 开发手册》背后的思考.md</a>

                </li>
                <li>

                    
                    <a href="认识&#32;MySQL&#32;和&#32;Redis&#32;的数据一致性问题.md">认识 MySQL 和 Redis 的数据一致性问题.md</a>

                </li>
                <li>

                    
                    <a href="进阶：Dockerfile&#32;高阶使用指南及镜像优化.md">进阶：Dockerfile 高阶使用指南及镜像优化.md</a>

                </li>
                <li>

                    
                    <a href="铁总在用的高性能分布式缓存计算框架&#32;Geode.md">铁总在用的高性能分布式缓存计算框架 Geode.md</a>

                </li>
                <li>

                    
                    <a href="阿里云PolarDB及其共享存储PolarFS技术实现分析（上）.md">阿里云PolarDB及其共享存储PolarFS技术实现分析（上）.md</a>

                </li>
                <li>

                    
                    <a href="阿里云PolarDB及其共享存储PolarFS技术实现分析（下）.md">阿里云PolarDB及其共享存储PolarFS技术实现分析（下）.md</a>

                </li>
                <li>

                    
                    <a href="面试最常被问的&#32;Java&#32;后端题.md">面试最常被问的 Java 后端题.md</a>

                </li>
                <li>

                    
                    <a href="领域驱动设计在互联网业务开发中的实践.md">领域驱动设计在互联网业务开发中的实践.md</a>

                </li>
                <li>

                    
                    <a href="领域驱动设计的菱形对称架构.md">领域驱动设计的菱形对称架构.md</a>

                </li>
                <li>

                    
                    <a href="高效构建&#32;Docker&#32;镜像的最佳实践.md">高效构建 Docker 镜像的最佳实践.md</a>

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
                        <div><h1>MySQL 故障诊断：一个 ALTER TALBE 执行了很久，你慌不慌？</h1>
<h3>先了解下 MySQL 数据字典</h3>
<p>当我们对一张大表执行了一个 ALTER TABLE 操作，执行了很久，也不知道是否执行完成，进程在那挂着，此时的你，干瞪眼，进度看不到，进程不敢杀，就问你慌不慌？</p>
<p>在具体解决这个慌乱之前，我们先了解下 MySQL 的数据字典。</p>
<p>数据字典我们用一句话来概括，就是数据的数据，用于查询数据库中数据的信息内容。</p>
<p>MySQL 在 5.7 开始，对数据字典的使用有了很大的改进，使用上更加的方便，提供的能力也更高。performance_schema 可以查询事务信息、获取元数据锁、跟踪事件、统计内存使用情况等等。</p>
<p>到这里你是不是发现了什么？</p>
<p>performance_schema 这个是什么，是不是用它来让我们解除慌张？</p>
<p>有关 MySQL 数据字典，可以看我的另外一个 Chat：</p>
<blockquote>
<p>[MySQL 地基基础：数据字典](./MySQL 地基基础：数据字典.md)</p>
</blockquote>
<h3>使用一些重要的重要功能</h3>
<p>既然了解到 MySQL 数据字典可以帮助我们，那它是如何实现呢？</p>
<p>我们先看看官网是如何解释的</p>
<blockquote>
<p><a href="https://dev.mysql.com/doc/refman/5.7/en/monitor-alter-table-performance-schema.html">https://dev.mysql.com/doc/refman/5.7/en/monitor-alter-table-performance-schema.html</a></p>
<p>You can monitor ALTER TABLE progress for InnoDB tables using Performance Schema.</p>
<p>There are seven stage events that represent different phases of ALTER TABLE. Each stage event reports a running total of WOR_COMPLETED and WORK_ESTIMATED for the overall ALTER TABLE operation as it progresses through its different phases. WORK_ESTIMATED is calculated using a formula that takes into account all of the work that ALTER TABLE performs, and may be revised during ALTER TABLE processing. WORK_COMPLETED and WORK_ESTIMATED values are an abstract representation of all of the work performed by ALTER TABLE.</p>
</blockquote>
<p>大意就是我们可以在 Performance Schema 看到 ALTER TABLE 的进度，包括执行的时间，大概剩余的时间。</p>
<p>想要使用这个能力，我们需要开启几个功能。</p>
<p><strong>Enable the stage/innodb/alter% instruments</strong></p>
<pre><code>mysql&gt; UPDATE performance_schema.setup_instruments
    -&gt;        SET ENABLED = 'YES'
    -&gt;        WHERE NAME LIKE 'stage/innodb/alter%';
Query OK, 0 rows affected (0.01 sec)
Rows matched: 7  Changed: 0  Warnings: 0
</code></pre>
<p><strong>Enable the stage event consumer tables</strong></p>
<pre><code>mysql&gt; UPDATE performance_schema.setup_consumers
    -&gt;        SET ENABLED = 'YES'
    -&gt;        WHERE NAME ='events_stages_current';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql&gt; UPDATE performance_schema.setup_consumers
    -&gt;        SET ENABLED = 'YES'
    -&gt;        WHERE NAME ='events_stages_history';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql&gt; UPDATE performance_schema.setup_consumers
    -&gt;        SET ENABLED = 'YES'
    -&gt;        WHERE NAME ='events_stages_history_long';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
</code></pre>
<p>功能开启了，接下来我们进行直观的验证环节。</p>
<h3>直观的观察事件执行进度</h3>
<p>首先，我们有一张大表（你可以用 SysBench 建一个，或者其他各种途径都可以），这里我已经有一张大表 sbtest.sbtest1，表结构如下：</p>
<pre><code>mysql&gt; desc sbtest.sbtest1;
+-------+-----------+------+-----+---------+----------------+
| Field | Type      | Null | Key | Default | Extra          |
+-------+-----------+------+-----+---------+----------------+
| id    | int(11)   | NO   | PRI | NULL    | auto_increment |
| k     | int(11)   | NO   | MUL | 0       |                |
| c     | char(120) | NO   |     |         |                |
| pad   | char(60)  | NO   |     |         |                |
+-------+-----------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
</code></pre>
<p>数据量 500W：</p>
<pre><code>mysql&gt; select count(*) from  sbtest.sbtest1;
+----------+
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (0.67 sec)
</code></pre>
<p>新增一个字段：</p>
<pre><code>mysql&gt; alter table sbtest.sbtest1 add d char(20);
</code></pre>
<p>重头戏来了，查看一下进度：</p>
<pre><code>mysql&gt; select * from performance_schema.events_stages_current\G;
*************************** 1. row ***************************
         THREAD_ID: 28
          EVENT_ID: 14
      END_EVENT_ID: NULL
        EVENT_NAME: stage/innodb/alter table (read PK and internal sort)
            SOURCE: 
       TIMER_START: 159726265417733000
         TIMER_END: 159819571346680000
        TIMER_WAIT: 93305928947000
    WORK_COMPLETED: 118256
    WORK_ESTIMATED: 302958
  NESTING_EVENT_ID: 13
NESTING_EVENT_TYPE: STATEMENT
1 row in set (0.00 sec)

......

mysql&gt; select * from performance_schema.events_stages_current\G;
*************************** 1. row ***************************
         THREAD_ID: 28
          EVENT_ID: 14
      END_EVENT_ID: NULL
        EVENT_NAME: stage/innodb/alter table (read PK and internal sort)
            SOURCE: 
       TIMER_START: 159726265417733000
         TIMER_END: 159910492100061000
        TIMER_WAIT: 184226682328000
    WORK_COMPLETED: 230688
    WORK_ESTIMATED: 302958
  NESTING_EVENT_ID: 13
NESTING_EVENT_TYPE: STATEMENT
1 row in set (0.01 sec)
</code></pre>
<p>多执行几次，发现数据是有变化的，这些内容代表了什么呢？</p>
<ul>
<li>THREAD_ID：线程 ID</li>
<li>EVENT_ID：事件 ID</li>
<li>END_EVENT_ID：结束事件 ID</li>
<li>EVENT_NAME：事件名称，说明了当前执行的事件</li>
<li>SOURCE：源码位置</li>
<li>TIMER_START：事件开始时间（皮秒）</li>
<li>TIMER_END：事件结束时间（皮秒，如果没有执行完成，时间就是当前之间）</li>
<li>TIMER_WAIT：事件等待事件（皮秒）</li>
<li>WORK_COMPLETED：任务完成情况</li>
<li>WORK_ESTIMATED：任务估算情况</li>
<li>NESTING_EVENT_ID：事件对应的父事件 ID</li>
<li>NESTING_EVENT_TYPE：父事件类型（STATEMENT、STAGE、WAIT）</li>
</ul>
<h3>收下这个常用的 SQL</h3>
<ol>
<li>查看事件任务完成情况：</li>
</ol>
<pre><code>mysql&gt; SELECT pt.INFO, ec.THREAD_ID, ec.EVENT_NAME, ec.WORK_COMPLETED, ec.WORK_ESTIMATED, pt.STATE FROM performance_schema.events_stages_current ec left join performance_schema.threads th on ec.thread_id = th.thread_id left join information_schema.PROCESSLIST pt on th.PROCESSLIST_ID = pt.ID where pt.INFO like 'ALTER%';
+-------------------------------------------+-----------+------------------------------------------------------+----------------+----------------+----------------+
| INFO                                      | THREAD_ID | EVENT_NAME                                           | WORK_COMPLETED | WORK_ESTIMATED | STATE          |
+-------------------------------------------+-----------+------------------------------------------------------+----------------+----------------+----------------+
| alter table sbtest.sbtest1 add d char(20) |        28 | stage/innodb/alter table (read PK and internal sort) |         201496 |         308223 | altering table |
+-------------------------------------------+-----------+------------------------------------------------------+----------------+----------------+----------------+
1 row in set (0.25 sec)
</code></pre>
<ol start="2">
<li>查看任务完成事件：</li>
</ol>
<pre><code>mysql&gt; select stmt.sql_text as sql_text, concat(work_completed, '/' , work_estimated) as progress, (stage.timer_end - stmt.timer_start) / 1e12 as current_seconds, (stage.timer_end - stmt.timer_start) / 1e12 * (work_estimated-work_completed) / work_completed as remaining_seconds from performance_schema.events_stages_current stage, performance_schema.events_statements_current stmt where stage.thread_id = stmt.thread_id and stage.nesting_event_id = stmt.event_id;
+-------------------------------------------+---------------+-----------------+--------------------+
| sql_text                                  | progress      | current_seconds | remaining_seconds  |
+-------------------------------------------+---------------+-----------------+--------------------+
| alter table sbtest.sbtest1 add d char(20) | 135192/308223 |   102.461512532 | 131.13954949201502 |
+-------------------------------------------+---------------+-----------------+--------------------+
1 row in set (0.00 sec)
</code></pre>
<h3>总结</h3>
<p>这样我们通过 MySQL 的这个数据字典就可以很直观地看到 ALTER 的执行情况了，当你看到这样的执行进度，是不是就不那么慌了。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;性能优化：碎片整理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;故障诊断：如何在日志中轻松定位大事务.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43633ccaab645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E6%96%87%E7%AB%A0/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
