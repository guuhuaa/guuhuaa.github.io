<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL 从一条数据说起-InnoDB行存储数据结构.md</title>
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

                    <a class="current-tab" href="MySQL&#32;从一条数据说起-InnoDB行存储数据结构.md">MySQL 从一条数据说起-InnoDB行存储数据结构.md</a>
                    

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

                    
                    <a href="MySQL&#32;故障诊断：一个&#32;ALTER&#32;TALBE&#32;执行了很久，你慌不慌？.md">MySQL 故障诊断：一个 ALTER TALBE 执行了很久，你慌不慌？.md</a>

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
                        <div><h1>MySQL 从一条数据说起-InnoDB行存储数据结构</h1>
<p>先给大家讲一个故事，我刚参加工作，在一个小作坊里面当【码畜】（尽管现在也是），有一天老板从我背后走过，说了一句举世震惊的话：我看你们的数据库和excel一样，不就是一行行数据，人家excel还可以对单元格进行美化，还有各种函数，生成各种报表，你们的数据库有什么复杂的？我竟无力反驳。</p>
<p>为什么要说这个故事呢，当然是为了引出今天的话题——InnoDB行存储数据结构。</p>
<p>虽然做开发的各位，或多或少都接触过数据库，但是数据库中的一行行数据到底是怎么存储的，存储的格式又是什么，就不是每个开发都知道的了，数据库对我们而言就是一个黑盒子，你想打开这个黑盒子一探究竟吗？【不，我不想，我只想CURD】【不，这不是你的真实想法】。当我们收了快递，尽管我们已经知道是什么快递了，但是我们还是会迫不及待的拆开快递，更何况，我们面对的是未知的事物，作为人的天性，一定是非常希望可以打开这个黑盒子，更别提充满好奇心的程序猿了，今天我就带着打开这神秘的黑盒子。</p>
<p>这次我们打开的黑盒子便是InnoDB存储数据结构，换而言之，MySql其他的存储引擎，如Memory，MyISAM不在本次的讨论范围。</p>
<h2>InnoDB页简介</h2>
<p>InnoDB是一个把数据存储在硬盘的存储引擎，即使服务器重启，数据依然不会丢失，而真正的数据处理是发生在内存中的，所以InnoDB需要把硬盘上数据加载到内存中，然后在内存中进行各种数据处理，最终在某个时机把内存中的数据刷新到硬盘。而硬盘的处理速度是很慢很慢的，和内存差的太远了，如果InnoDB每次只从硬盘中读取一条数据，显然是不行的，速度会慢死，所以InnoDB会把数据分成若干页，以页作为内存和硬盘之间交互的基本单位，说的再直白点：InnoDB读取数据不是一行一行读，而是以页为最小单位读取数据。默认情况下，一页是16K，也就是InnoDB读取数据的数据大小至少是16K。当然这个值是可以被修改的，因为一般情况下，也没人会修改这个值，所以这里我就不说明应该怎么改了。</p>
<h2>InnoDB行格式</h2>
<p>之所以，文章开头的老板会认为数据库和excel是一样的，就是因为我们平时基本都是用可视化工具去管理表，去查数据，一个不懂的人乍一看，确实和excel有点像，就是一行一行数据，这些数据在硬盘上存储格式是需要我们去探究的。</p>
<p>InnoDB提供了4种行格式供我们选择，分别是Compact、Redundant、Dynamic和Compressed行格式，以后可能会有新的行格式出现，但是区别并不是很大。</p>
<p>我们建表的时候，可以指定某种行格式：</p>
<pre><code>CREATE TABLE table_name (列信息) ROW_FORMAT=行格式名称
</code></pre>
<p>也可以修改已经存在的表的行格式：</p>
<pre><code>ALTER TABLE  table_name ROW_FORMAT=行格式名称
</code></pre>
<h2>准备工作</h2>
<p>为了后面的故事可以顺利展开，我们先来建一张表：</p>
<pre><code>CREATE TABLE  hero(
`x` VARCHAR(10),
`y` VARCHAR(10) NOT NULL,
`z` CHAR(10),
`t` VARCHAR(10)
)CHARSET=ASCII, ROW_FORMAT=COMPACT;
</code></pre>
<p>我建了一张表，指定的行格式是COMPACT，采用的字符集是ASCII，也就是我们的中文是无法存进去的，现在我要向这张表添加两行数据：</p>
<pre><code>INSERT INTO hero(x, y, z, t) VALUES('a', 'bb', 'cccc', 'ddddd'), ('a', 'b', NULL, NULL);
</code></pre>
<p>现在表中的数据是这样的：
<img src="assets/15100432-eedffb54dcdcbcbb.png" alt="image.png" /></p>
<p>表建好了，数据填充好了，下面我们就来分析下在COMPACT行格式下，数据是如何存储的吧。</p>
<h2>COMPACT行格式</h2>
<p><img src="assets/15100432-971e813ef0d2285b.png" alt="image.png" /></p>
<p>从上图可以看到，一行数据被分为了两个部分，一部分是记录的额外信息，一部分是记录的真实数据。</p>
<h3>记录额外信息</h3>
<h4>变长字段字节数列表</h4>
<p>varchar(X)和char(X)的区别是什么，相信大家都非常清楚，char是定长的，varchar是变长的，变长字段中存储多少字节的数据不是固定的，所以InnoDB在存储数据的时候，会把这些数据占用的真实字节数也保存下来，也就是变长字段是占用了两部分空间来存储的：</p>
<ol>
<li>真实的数据内容</li>
<li>占用的字节数</li>
</ol>
<p>在COMPACT行格式中，把所有的变长字段所占用的字节数逆序排放在变长字段字节数列表中。</p>
<p>我们先前创建了一张表，还准备了两条数据，现在我们来看下第一条数据中的变长字段字节数列表是什么酱紫的。</p>
<p>表中有四个字段，其中x，y，t三个字段都是变长字段，所以这三个字段的字节数需要保存在变长字段字节数列表，数据表采用的字符集是ascii，所以每一个字符占用的字节数是1，下面我们来看下第一条数据各个变长字段所占用的字节数：</p>
<table>
<thead>
<tr>
<th>字段名称</th>
<th>内容</th>
<th>占用字节数 （十进制）</th>
<th>占用字节数 （十六进制）</th>
</tr>
</thead>
<tbody>
<tr>
<td>x</td>
<td>a</td>
<td>1</td>
<td>0x01</td>
</tr>
<tr>
<td>y</td>
<td>bb</td>
<td>2</td>
<td>0x02</td>
</tr>
<tr>
<td>t</td>
<td>ddddd</td>
<td>5</td>
<td>0x05</td>
</tr>
</tbody>
</table>
<p>所以，第一行数据x，y，t三个字段所占用的字节数分别是1 2 5，但是InnoDB会把所占用的字节数逆序排放，如果用16进制来表示变长字段所占用的字节数就是这样的效果了：
<img src="assets/15100432-4bab1ecbf7cc93ca.png" alt="image.png" /></p>
<p><em>为了更容易理解、清晰，所以我用了空格来分割，其实是没有的。</em></p>
<p>由于数据的长度都比较小，用一个字节就可以表示，但是如果变长字段占用的字节数比较多，就要用两个字节来表示了，到底使用一个字节来表示，还是用两个字节来表示，InnoDB有着自己的一套规则。在说这个规则之前，要先说明下规则中用到的三个变量：</p>
<ol>
<li>W：指定字符集下，一个字符最多需要占用的字节数。比如，ascii字符集的W是1，GBK字符集的W是2，utf-8字符集的W是3。</li>
<li>M：最多可以存储多少个字符，varchar(50)的M就是50。</li>
<li>L：实际存储字符占用了多少字节。</li>
</ol>
<p>W*M：指定字段类型、字符集下，存储的字符串最多占用的字节数。</p>
<p>下面就是规则了：</p>
<ol>
<li>如果M*W&lt;=255，那么用一个字节表示字符串所占用的字节数。</li>
<li>如果M*W&gt;255，则分为两种情况：
2.1 如果L&lt;=127，则用一个字节来表示字符串所占用的字节数。
2.2 如果L&gt;127，则用两个字节来表示字符串所占用的字节数。</li>
</ol>
<p>光看规则是不是觉得很绕，总结一下，该可变字段允许存储的最大字节数(W*M)&gt;255，且真实存储的字节数(L)超过127，就用两个字节来表示字符串所占用的字节数，否则用一个字节来表示字符串所占用的字节数。</p>
<p>我们再来看看第二条数据，字段t的值是NULL，变长字段字节数列表只存储非NULL列内容占用的字节数，所以对于第二条数据，变长字段字节数列表只要存储x和y所占用的字节数即可，填充在变长字段字节数列表的效果是酱紫的：
<img src="assets/15100432-6b4bf28a7a2d82bd.png" alt="image.png" /></p>
<p>变长字段字节数列表不是必须的，如果一个表中所有的字段都不是变长的，那么就没有变长字段字节数列表了。</p>
<p>我们建的表采用的字符集是ascii编码的，一个字符所占用的字节固定是1，如果我们采用utf-8字符集，一个字段所占用的字节就不是固定的了，而是一个范围：1-3，所以如果我们采用这样的字符集，char(m)虽然是定长字段，但是也会被加入到变长字段字节数列表中。</p>
<h4>NULL值列表</h4>
<p>我待过一家公司，对表设计有非常明确的规定，其中有一条是任何字段都不允许为NULL，问原因，DBA只是淡淡的说了句，允许为NULL会额外占用一些空间。我也没有继续追究下去，就按照规定来呗。下面我就来揭秘为什么会有这个蛋疼的规定。</p>
<p>如果表中有字段允许为NULL，InnoDB就会开辟一块空间来标识每个字段实际存储的数据是不是为NULL，如果表中的字段都不允许为NULL，那么这块空间就不复存在了。</p>
<p>那么InnoDB开辟出来的那块空间具体是怎么回事呢，接下去往下看。</p>
<p>每个允许存储为NULL的字段对应一个二进制位：</p>
<ul>
<li>如果字段实际存储的数据不为NULL，二进制是0。</li>
<li>如果字段实际存储的数据是NULL，二进制是1。</li>
</ul>
<p>这里和变长字段字节数列表是一样的，是逆序排放的。</p>
<p>我们新建的hero表有三个字段都允许为NULL，所以存在NULL值列表。</p>
<p>我们先来看第一条数据，三个字段存储的实际数据都不为NULL，所以用二进制来表示是酱紫的：
<img src="assets/15100432-8a4f9cfb17202e7f.png" alt="image.png" /></p>
<p>但是InnoDB是用整数字节的二进制位来表示NULL值列表的，现在不足8位，所以要在高位补0，最终用二进制来表示是酱紫的：
<img src="assets/15100432-2be184c3358e38ac.png" alt="image.png" /></p>
<p>所以，对于第一条数据，NULL值列表用十六进制表示是0x00。</p>
<p>我们再来看看第二条数据，其中z和t两个字段存储的实际数据都是NULL，我们来看看用二进制如何来表示：
<img src="assets/15100432-95eeef6437382e3e.png" alt="image.png" /></p>
<p>同样的，需要高位补0：
<img src="assets/15100432-cb2ba643784395da.png" alt="image.png" /></p>
<p>所以，对于第二条数据，NULL值列表用十六进制表示是0x06。</p>
<p>我们把两条数据的NULL值列表都填充完毕是酱紫的效果：
<img src="assets/15100432-561973f9ad46fe33.png" alt="image.png" /></p>
<h4>记录头信息</h4>
<p>记录头信息中包含的内容很多，我先随便列举几条：</p>
<ol>
<li>delete_mask ：标识此条数据是否被删除。</li>
<li>next_record：下一条数据的位置。</li>
<li>record_type：表示当前记录的类型，0表示普通记录，1表示B+树非叶子节点记录，2表示最小记录，3表示最大记录
...
还有其他的，或者更具体的解释等以后用到了再说吧。</li>
</ol>
<h3>记录真实数据</h3>
<p>对于hero表来说，记录真实数据部分除了我们定义的四个字段，还有三个隐藏字段，分别为：row_id、trx_id、roll_pointer，我们来看下这三个字段是什么。</p>
<h4>row_id</h4>
<p>如果我们建表的时候指定了主键或者唯一约束列，那么就没有row_id隐藏字段了。如果既没有指定主键，又没有唯一约束，那么InnoDB就会为记录添加row_id隐藏字段。row_id不是必需的，占用6个字节。</p>
<h4>trx_id</h4>
<p>事务Id，表示这个数据是由哪个事务生成的。 trx_id是必需的，占用6个字节。</p>
<h4>roll_pointer</h4>
<p>这条数据上一个版本的指针。roll_pointer是必需的，占用7个字节。</p>
<p>关于 trx_id、roll_pointer的具体解释，在我上一篇关于事务的博客有详细描述过，感兴趣的小伙伴可以找来看看。</p>
<h3>VARCHAR(M)最多能存储的数据</h3>
<p>在讲可变字段字节数列表的时候，讲到InnoDB会有一套规则，计算是用一个字节来表示实际存储的字节数，还是用两个字节来表示实际存储的字节数，但是如果存储的字符串很长很长，用两个字节都无法表示，该怎么办呢？</p>
<p>我们先来看看用两个字节最多可以表示的字节数是多少：
<img src="assets/15100432-d5e62af469ef9e03.png" alt="image.png" />
用两个字节最多可以表示的字节数是65535。</p>
<p>我们用这个最大字节数来试下，能不能成功创建一张表：</p>
<pre><code>CREATE TABLE test_max ( test VARCHAR ( 65535 ) ) charset = ascii,
row_format = Compact
Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs
</code></pre>
<p>看到了木有，两个字节最多可以表示的字节数是65535，我们用这个数字创建表竟然失败了，更别提65536了。</p>
<p>为什么失败呢？</p>
<p>从报错信息就可以知道一行数据的最大字节数是65535，其中包含了storage overhead。问题来了，这个storage overhead是什么呢？就是可变字段字节数列表、NULL值列表。</p>
<p>我们存储VARCHAR(M)类型的字段，其实可能分成了三个部分来存储：</p>
<ul>
<li>真实数据</li>
<li>真实数据占用的字节数</li>
<li>NULL标识，如果不允许为NUL，这部分不需要</li>
</ul>
<p>刚刚我们尝试创建的表，字段是允许为NULL的，所以会占用一个字节来存储NULL标识，真实的数据所占的字节数用两个字节来表示，所以最多可以存储65535-2-1=65532个字节。</p>
<pre><code>CREATE TABLE test_max ( test VARCHAR ( 65532 ) ) charset = ascii,
row_format = Compact
&gt; OK
&gt; 时间: 0.229s
</code></pre>
<p>我们新建的表采用的字符集是ascii，如果采用的是GBK或者UTF-8，VARCHAR(M)最多能存储的数据计算方式就不一样了：</p>
<ul>
<li>在GBK字符集下，一个字符最多需要两个字节，VARCHAR(M)的最大取值就是 65532/2=32766。</li>
<li>在UTF-8字符集下，一个字符串最多需要三个字节，VARCHAR(M)的最大取值就是 65532/3=21844。</li>
</ul>
<p>我们上面所说的只是针对于一个列的计算方式，如果有多个列的话，要保证多个列所允许占用的最大字节数+变长字段字节数列表所占用的字节数+NULL值列表所占用的字节数&lt;=65535。</p>
<h3>行溢出</h3>
<p>文章开头的时候，给大家简单的介绍了下页的概念，我们知道硬盘和内存之间交互的基本单位是页，而页的大小默认情况下16K，也就是16384字节，而VARCHAR(M)最多可以存储的远远不止16384字节，这样就出现了一个页存放不了一条记录的局面。</p>
<p>在Compact和Redundant行格式中，对于占用字节数非常大的列，在记录的真实数据中只会存储一小部分数据（768个字节），剩余的数据分散存储在其他的页，为了可以找到它们，在记录的真实数据中会记录这些页的地址，就像下面酱紫：
<img src="assets/15100432-d1d7c9453a175c67.png" alt="image.png" /></p>
<h2>Dynamic和Compressed行格式</h2>
<p>Dynamic和Compressed行格式和COMPACT行格式很相近，只是在行溢出的处理方式上有所不同，溢出后，Dynamic和Compressed行格式不会在记录的真实数据中存储一小部分数据，而是直接记录其他页的地址。Dynamic和Compressed行格式的区别是Compressed格式会对页进行压缩以节省空间。</p>
<p>Redundant行格式是MySql5.0之前使用的，现在基本不会再使用，这里就不介绍了。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;亿级别数据迁移实战代码分享.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;地基基础：事务和锁的面纱.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43631b0b70645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
