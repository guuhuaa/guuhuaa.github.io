<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL · 引擎特性 · InnoDB崩溃恢复.md</title>
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

                    <a class="current-tab" href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB崩溃恢复.md">MySQL · 引擎特性 · InnoDB崩溃恢复.md</a>
                    

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
                        <div><h1>MySQL · 引擎特性 · InnoDB崩溃恢复</h1>
<h2>前言</h2>
<p>数据库系统与文件系统最大的区别在于数据库能保证操作的原子性，一个操作要么不做要么都做，即使在数据库宕机的情况下，也不会出现操作一半的情况，这个就需要数据库的日志和一套完善的崩溃恢复机制来保证。本文仔细剖析了InnoDB的崩溃恢复流程，代码基于5.6分支。</p>
<h2>基础知识</h2>
<p>**lsn: ** 可以理解为数据库从创建以来产生的redo日志量，这个值越大，说明数据库的更新越多，也可以理解为更新的时刻。此外，每个数据页上也有一个lsn，表示最后被修改时的lsn，值越大表示越晚被修改。比如，数据页A的lsn为100，数据页B的lsn为200，checkpoint lsn为150，系统lsn为300，表示当前系统已经更新到300，小于150的数据页已经被刷到磁盘上，因此数据页A的最新数据一定在磁盘上，而数据页B则不一定，有可能还在内存中。
**redo日志: ** 现代数据库都需要写redo日志，例如修改一条数据，首先写redo日志，然后再写数据。在写完redo日志后，就直接给客户端返回成功。这样虽然看过去多写了一次盘，但是由于把对磁盘的随机写入(写数据)转换成了顺序的写入(写redo日志)，性能有很大幅度的提高。当数据库挂了之后，通过扫描redo日志，就能找出那些没有刷盘的数据页(在崩溃之前可能数据页仅仅在内存中修改了，但是还没来得及写盘)，保证数据不丢。
**undo日志: ** 数据库还提供类似撤销的功能，当你发现修改错一些数据时，可以使用rollback指令回滚之前的操作。这个功能需要undo日志来支持。此外，现代的关系型数据库为了提高并发(同一条记录，不同线程的读取不冲突，读写和写读不冲突，只有同时写才冲突)，都实现了类似MVCC的机制，在InnoDB中，这个也依赖undo日志。为了实现统一的管理，与redo日志不同，undo日志在Buffer Pool中有对应的数据页，与普通的数据页一起管理，依据LRU规则也会被淘汰出内存，后续再从磁盘读取。与普通的数据页一样，对undo页的修改，也需要先写redo日志。
**检查点: ** 英文名为checkpoint。数据库为了提高性能，数据页在内存修改后并不是每次都会刷到磁盘上。checkpoint之前的数据页保证一定落盘了，这样之前的日志就没有用了(由于InnoDB redolog日志循环使用，这时这部分日志就可以被覆盖)，checkpoint之后的数据页有可能落盘，也有可能没有落盘，所以checkpoint之后的日志在崩溃恢复的时候还是需要被使用的。InnoDB会依据脏页的刷新情况，定期推进checkpoint，从而减少数据库崩溃恢复的时间。检查点的信息在第一个日志文件的头部。
**崩溃恢复: ** 用户修改了数据，并且收到了成功的消息，然而对数据库来说，可能这个时候修改后的数据还没有落盘，如果这时候数据库挂了，重启后，数据库需要从日志中把这些修改后的数据给捞出来，重新写入磁盘，保证用户的数据不丢。这个从日志中捞数据的过程就是崩溃恢复的主要任务，也可以成为数据库前滚。当然，在崩溃恢复中还需要回滚没有提交的事务，提交没有提交成功的事务。由于回滚操作需要undo日志的支持，undo日志的完整性和可靠性需要redo日志来保证，所以崩溃恢复先做redo前滚，然后做undo回滚。</p>
<p>我们从源码角度仔细剖析一下数据库崩溃恢复过程。整个过程都在引擎初始化阶段完成(<code>innobase_init</code>)，其中最主要的函数是<code>innobase_start_or_create_for_mysql</code>，innodb通过这个函数完成创建和初始化，包括崩溃恢复。首先来介绍一下数据库的前滚。</p>
<h2>redo日志前滚数据库</h2>
<p>前滚数据库，主要分为两阶段，首先是日志扫描阶段，扫描阶段按照数据页的space_id和page_no分发redo日志到hash_table中，保证同一个数据页的日志被分发到同一个哈希桶中，且按照lsn大小从小到大排序。扫描完后，再遍历整个哈希表，依次应用每个数据页的日志，应用完后，在数据页的状态上至少恢复到了崩溃之前的状态。我们来详细分析一下代码。
首先，打开所有的ibdata文件(<code>open_or_create_data_files</code>)(ibdata可以有多个)，每个ibdata文件有个flush_lsn在头部，计算出这些文件中的max_flush_lsn和min_flush_lsn，因为ibdata也有可能有数据没写完整，需要恢复，后续(<code>recv_recovery_from_checkpoint_start_func</code>)通过比较checkpont_lsn和这两个值来确定是否需要对ibdata前滚。
接着，打开系统表空间和日志表空间的所有文件(<code>fil_open_log_and_system_tablespace_files</code>)，防止出现文件句柄不足，清空buffer pool(<code>buf_pool_invalidate</code>)。接下来就进入最最核心的函数:recv_recovery_from_checkpoint_start_func，注意，即使数据库是正常关闭的，也会进入。
虽然<code>recv_recovery_from_checkpoint_start_func</code>看过去很冗长，但是很多代码都是为了LOG_ARCHIVE特性而编写的，真正数据崩溃恢复的代码其实不多。
首先，初始化一些变量，查看<code>srv_force_recovery</code>这个变量，如果用户设置跳过前滚阶段，函数直接返回。
接着，初始化<code>recv_sys</code>结构，分配hash_table的大小，同时初始化flush list rbtree。<code>recv_sys</code>结构主要在崩溃恢复前滚阶段使用。hash_table就是之前说的用来存不同数据页日志的哈希表，哈希表的大小被初始化为buffer_size_in_bytes/512, 这个是哈希表最大的长度，超过就存不下了，幸运的是，需要恢复的数据页的个数不会超过这个值，因为buffer poll最多(数据库崩溃之前脏页的上线)只能存放buffer_size_in_bytes/16KB个数据页，即使考虑压缩页，最多也只有buffer_size_in_bytes/1KB个，此外关于这个哈希表内存分配的大小，可以参考bug#53122。flush list rbtree这个主要是为了加入插入脏页列表，InnoDB的flush list必须按照数据页的最老修改lsn(oldest_modifcation)从小到大排序，在数据库正常运行时，可以通过log_sys-&gt;mutex和log_sys-&gt;log_flush_order_mutex保证顺序，在崩溃恢复则没有这种保证，应用数据的时候，是从第一个元素开始遍历哈希表，不能保证数据页按照最老修改lsn(oldest_modifcation)从小到大排序，这样就需要线性遍历flush_list来寻找插入位置，效率太低，因此引入红黑树，加快查找插入的位置。
接着，从ib_logfile0的头中读取checkpoint信息，主要包括checkpoint_lsn和checkpoint_no。由于InnoDB日志是循环使用的，且最少要有2个，所以ib_logfile0一定存在，把checkpoint信息存在里面很安全，不用担心被删除。checkpoint信息其实会写在文件头的两个地方，两个checkpoint域轮流写。为什么要两个地方轮流写呢？假设只有一个checkpoint域，一直更新这个域，而checkpoint域有512字节(<code>OS_FILE_LOG_BLOCK_SIZE</code>)，如果刚好在写这个512字节的时候，数据库挂了，服务器也挂了(先不考虑硬件的原子写特性，早期的硬件没有这个特性)，这个512字节可能只写了一半，导致整个checkpoint域不可用。这样数据库将无法做崩溃恢复，从而无法启动。如果有两个checkpoint域，那么即使一个写坏了，还可以用另外一个尝试恢复，虽然有可能这个时候日志已经被覆盖，但是至少提高了恢复成功的概率。两个checkpoint域轮流写，也能减少磁盘扇区故障带来的影响。checkpoint_lsn之前的数据页都已经落盘，不需要前滚，之后的数据页可能还没落盘，需要重新恢复出来，即使已经落盘也没关系，因为redo日志时幂等的，应用一次和应用两次都一样(底层实现: 如果数据页上的lsn大于等于当前redo日志的lsn，就不应用，否则应用。checkpoint_no可以理解为checkpoint域写盘的次数，每次刷盘递增1，同时这个值取模2可以用来实现checkpoint_no域的轮流写。正常逻辑下，选取checkpoint_no值大的作为最终的checkpoint信息，用来做后续崩溃恢复扫描的起始点。
接着，使用checkpoint域的信息初始化recv_sys结构体的一些信息后，就进入日志解析的核心函数<code>recv_group_scan_log_recs</code>，这个函数后续我们再分析，主要作用就是解析redo日志，如果内存不够了，就直接调用应用(<code>recv_apply_hashed_log_recs</code>)日志，然后再接着解析。如果需要应用的日志很少，就仅仅解析分发日志，到<code>recv_recovery_from_checkpoint_finish</code>函数中在应用日志。
接着，依据当前刷盘的数据页状态做一次checkpoint，因为在<code>recv_group_scan_log_recs</code>里可能已经应用部分日志了。至此<code>recv_recovery_from_checkpoint_start_func</code>函数结束。
在<code>recv_recovery_from_checkpoint_finish</code>函数中，如果srv_force_recovery设置正确，就开始调用函数<code>recv_apply_hashed_log_recs</code>应用日志，然后等待刷脏的线程退出(线程是崩溃恢复时临时启动的)，最后释放recv_sys的相关资源以及hash_table占用的内存。
至此，数据库前滚结束。接下来，我们详细分析一下redo日志解析函数以及redo日志应用函数的实现细节。</p>
<h2>redo日志解析函数</h2>
<p>解析函数的最上层是<code>recv_group_scan_log_recs</code>，这个函数调用底层函数(<code>log_group_read_log_seg</code>)，按照RECV_SCAN_SIZE(64KB)大小分批读取。读取出来后，首先通过block_no和lsn之间的关系以及日志checksum判断是否读到了日志最后(所以可以看出，并没一个标记在日志头标记日志的有效位置，完全是按照上述两个条件判断是否到达了日志尾部)，如果读到最后则返回(之前说了，即使数据库是正常关闭的，也要走崩溃恢复逻辑，那么在这里就返回了，因为正常关闭的checkpoint值一定是指向日志最后)，否则则把日志去头掐尾放到一个recv_sys-&gt;buf中，日志头里面存了一些控制信息和checksum值，只是用来校验和定位，在真正的应用中没有用。在放到recv_sys-&gt;buf之前，需要检验一下recv_sys-&gt;buf有没有满(<code>RECV_PARSING_BUF_SIZE</code>，2M)，满了就报错(如果上一批解析有不完整的日志，日志解析函数不会分发，而是把这些不完整的日志留在recv_sys-&gt;buf中，直到解析到完整的日志)。接下的事情就是从recv_sys-&gt;buf中解析日志(<code>recv_parse_log_recs</code>)。日志分两种：single_rec和multi_rec，前者表示只对一个数据页进行一种操作，后者表示对一个或者多个数据页进行多种操作。日志中还包括对应数据页的space_id，page_no，操作的type以及操作的内容(<code>recv_parse_log_rec</code>)。解析出相应的日志后，按照space_id和page_no进行哈希(如果对应的表空间在内存中不存在，则表示表已经被删除了)，放到hash_table里面(日志真正存放的位置依然在buffer pool)即可，等待后续应用。这里有几个点值得注意：</p>
<ul>
<li>如果是multi_rec类型，则只有遇到MLOG_MULTI_REC_END这个标记，日志才算完整，才会被分发到hash_table中。查看代码，我们可以发现multi_rec类型的日志被解析了两次，一次用来校验完整性(寻找MLOG_MULTI_REC_END)，第二次才用来分发日志，感觉这是一个可以优化的点。</li>
<li>目前日志的操作type有50多种，每种操作后面的内容都不一样，所以长度也不一样，目前日志的解析逻辑，需要依次解析出所有的内容，然后确定长度，从而定位下一条日志的开始位置。这种方法效率略低，其实可以在每种操作的头上加上一个字段，存储后面内容的长度，这样就不需要解析太多的内容，从而提高解析速度，进一步提高崩溃恢复速度，从结果看，可以提高一倍的速度(从38秒到14秒，详情可以参见bug#82937)。</li>
<li>如果发现checkpoint之后还有日志，说明数据库之前没有正常关闭，需要做崩溃恢复，因此需要做一些额外的操作(<code>recv_init_crash_recovery</code>)，比如在错误日志中打印我们常见的“Database was not shutdown normally!”和“Starting crash recovery.”，还要从double write buffer中检查是否发生了数据页半写，如果有需要恢复(<code>buf_dblwr_process</code>)，还需要启动一个线程用来刷新应用日志产生的脏页(因为这个时候buf_flush_page_cleaner_thread还没有启动)。最后还需要打开所有的表空间。。注意是所有的表。。。我们在阿里云RDS MySQL的运维中，常常发现数据库hang在了崩溃恢复阶段，在错误日志中有类似“Reading tablespace information from the .ibd files...”字样，这就表示数据库正在打开所有的表，然后一看表的数量，发现有几十甚至上百万张表。。。数据库之所以要打开所有的表，是因为在分发日志的时候，需要确定space_id对应哪个ibd文件，通过打开所有的表，读取space_id信息来确定，另外一个原因是方便double write buffer检查半写数据页。针对这个表数量过多导致恢复过慢的问题，MySQL 5.7做了优化，WL#7142， 主要思想就是在每次checkpoint后，在第一次修改某个表时，先写一个新日志mlog_file_name(包括space_id和filename的映射)，来表示对这个表进行了操作，后续对这个表的操作就不用写这个新日志了，当需要崩溃恢复时候，多一次扫描，通过搜集mlog_file_name来确定哪些表被修改过，这样就不需要打开所有的表来确定space_id了。</li>
<li>最后一个值得注意的地方是内存。之前说过，如果有太多的日志已经被分发，占用了太多的内存，日志解析函数会在适当的时候应用日志，而不是等到最后才一起应用。那么问题来了，使用了多大的内存就会出发应用日志逻辑。答案是：buffer_pool_size_in_bytes - 512 * buffer_pool_instance_num * 16KB。由于buffer_pool_instance_num一般不会太大，所以可以任务，buffer pool的大部分内存都被用来存放日志。剩下的那些主要留给应用日志时读取的数据页，因为目前来说日志应用是单线程的，读取一个日志，把所有日志应用完，然后就可以刷回磁盘了，不需要太多的内存。</li>
</ul>
<h2>redo日志应用函数</h2>
<p>应用日志的上层函数为<code>recv_apply_hashed_log_recs</code>(应用日志也可能在io_helper函数中进行)，主要作用就是遍历hash_table，从磁盘读取对每个数据页，依次应用哈希桶中的日志。应用完所有的日志后，如果需要则把buffer_pool的页面都刷盘，毕竟空间有限。有以下几点值得注意：</p>
<ul>
<li>同一个数据页的日志必须按照lsn从小到大应用，否则数据会被覆盖。只应用redo日志lsn大于page_lsn的日志，只有这些日志需要重做，其余的忽略。应用完日志后，把脏页加入脏页列表，由于脏页列表是按照最老修改lsn(oldest_modification)来排序的，这里通过引入一颗红黑树来加速查找插入的位置，时间复杂度从之前的线性查找降为对数级别。</li>
<li>当需要某个数据页的时候，如果发现其没有在Buffer Pool中，则会查看这个数据页周围32个数据页，是否也需要做恢复，如果需要则可以一起读取出来，相当于做了一次io合并，减少io操作(<code>recv_read_in_area</code>)。由于这个是异步读取，所以最终应用日志的活儿是由io_helper线程来做的(<code>buf_page_io_complete</code>)，此外，为了防止短时间发起太多的io，在代码中加了流量控制的逻辑(<code>buf_read_recv_pages</code>)。如果发现某个数据页在内存中，则直接调用<code>recv_recover_page</code>应用日志。由此我们可以看出，InnoDB应用日志其实并不是单线程的来应用日志的，除了崩溃恢复的主线程外，io_helper线程也会参与恢复。并发线程数取决于io_helper中读取线程的个数。</li>
</ul>
<p>执行完了redo前滚数据库，数据库的所有数据页已经处于一致的状态，undo回滚数据库就可以安全的执行了。数据库崩溃的时候可能有一些没有提交的事务或者已经提交的事务，这个时候就需要决定是否提交。主要分为三步，首先是扫描undo日志，重新建立起undo日志链表，接着是，依据上一步建立起的链表，重建崩溃前的事务，即恢复当时事务的状态。最后，就是依据事务的不同状态，进行回滚或者提交。</p>
<h2>undo日志回滚数据库</h2>
<p>在<code>recv_recovery_from_checkpoint_start_func</code>之后，<code>recv_recovery_from_checkpoint_finish</code>之前，调用了<code>trx_sys_init_at_db_start</code>，这个函数做了上述三步中的前两步。
第一步在函数<code>trx_rseg_array_init</code>中处理，遍历整个undo日志空间(最多TRX_SYS_N_RSEGS(128)个segment)，如果发现某个undo segment非空，就进行初始化(<code>trx_rseg_create_instance</code>)。整个每个undo segment，如果发现undo slot非空(最多TRX_RSEG_N_SLOTS(1024)个slot)，也就行初始化(<code>trx_undo_lists_init</code>)。在初始化undo slot后，就把不同类型的undo日志放到不同链表中(<code>trx_undo_mem_create_at_db_start</code>)。undo日志主要分为两种：TRX_UNDO_INSERT和TRX_UNDO_UPDATE。前者主要是提供给insert操作用的，后者是给update和delete操作使用。之前说过，undo日志有两种作用，事务回滚时候用和MVCC快照读取时候用。由于insert的数据不需要提供给其他线程用，所以只要事务提交，就可以删除TRX_UNDO_INSERT类型的undo日志。TRX_UNDO_UPDATE在事务提交后还不能删除，需要保证没有快照使用它的时候，才能通过后台的purge线程清理。
第二步在函数<code>trx_lists_init_at_db_start</code>中进行，由于第一步中，已经在内存中建立起了undo_insert_list和undo_update_list(链表每个undo segment独立)，所以这一步只需要遍历所有链表，重建起事务的状态(<code>trx_resurrect_insert</code>和<code>trx_resurrect_update</code>)。简单的说，如果undo日志的状态是TRX_UNDO_ACTIVE，则事务的状态为TRX_ACTIVE，如果undo日志的状态是TRX_UNDO_PREPARED，则事务的状态为TRX_PREPARED。这里还要考虑变量srv_force_recovery的设置，如果这个变量值为非0，所有的事务都会回滚(即事务被设置为TRX_ACTIVE)，即使事务的状态应该为TRX_STATE_PREPARED。重建起事务后，按照事务id加入到trx_sys-&gt;trx_list链表中。最后，在函数<code>trx_sys_init_at_db_start</code>中，会统计所有需要回滚的事务(事务状态为TRX_ACTIVE)一共需要回滚多少行数据，输出到错误日志中，类似：5 transaction(s) which must be rolled back or cleaned up。InnoDB: in total 342232 row operations to undo的字样。
第三步的操作在两个地方被调用。一个是在<code>recv_recovery_from_checkpoint_finish</code>的最后，另外一个是在<code>recv_recovery_rollback_active</code>中。前者主要是回滚对数据字典的操作，也就是回滚DDL语句的操作，后者是回滚DML语句。前者是在数据库可提供服务之前必须完成，后者则可以在数据库提供服务(也即是崩溃恢复结束)之后继续进行(通过新开一个后台线程<code>trx_rollback_or_clean_all_recovered</code>来处理)。因为InnoDB认为数据字典是最重要的，必须要回滚到一致的状态才行，而用户表的数据可以稍微慢一点，对外提供服务后，慢慢恢复即可。因此我们常常在会发现数据库已经启动起来了，然后错误日志中还在不断的打印回滚事务的信息。事务回滚的核心函数是<code>trx_rollback_or_clean_recovered</code>，逻辑很简单，只需要遍历trx_sys-&gt;trx_list，按照事务不同的状态回滚或者提交即可(<code>trx_rollback_resurrected</code>)。这里要注意的是，如果事务是TRX_STATE_PREPARED状态，那么在InnoDB层，不做处理，需要在Server层依据binlog的情况来决定是否回滚事务，如果binlog已经写了，事务就提交，因为binlog写了就可能被传到备库，如果主库回滚会导致主备数据不一致，如果binlog没有写，就回滚事务。</p>
<h2>崩溃恢复相关参数解析</h2>
<p>**innodb_fast_shutdown: **
innodb_fast_shutdown = 0。这个表示在MySQL关闭的时候，执行slow shutdown，不但包括日志的刷盘，数据页的刷盘，还包括数据的清理(purge)，ibuf的合并，buffer pool dump以及lazy table drop操作(如果表上有未完成的操作，即使执行了drop table且返回成功了，表也不一定立刻被删除)。
innodb_fast_shutdown = 1。这个是默认值，表示在MySQL关闭的时候，仅仅把日志和数据刷盘。
innodb_fast_shutdown = 2。这个表示关闭的时候，仅仅日志刷盘，其他什么都不做，就好像MySQL crash了一样。
这个参数值越大，MySQL关闭的速度越快，但是启动速度越慢，相当于把关闭时候需要做的工作挪到了崩溃恢复上。另外，如果MySQL要升级，建议使用第一种方式进行一次干净的shutdown。</p>
<p>**innodb_force_recovery: **
这个参数主要用来控制InnoDB启动时候做哪些工作，数值越大，做的工作越少，启动也更加容易，但是数据不一致的风险也越大。当MySQL因为某些不可控的原因不能启动时，可以设置这个参数，从1开始逐步递增，知道MySQL启动，然后使用SELECT INTO OUTFILE把数据导出，尽最大的努力减少数据丢失。
innodb_force_recovery = 0。这个是默认的参数，启动的时候会做所有的事情，包括redo日志应用，undo日志回滚，启动后台master和purge线程，ibuf合并。检测到了数据页损坏了，如果是系统表空间的，则会crash，用户表空间的，则打错误日志。
innodb_force_recovery = 1。如果检测到数据页损坏了，不会crash也不会报错(<code>buf_page_io_complete</code>)，启动的时候也不会校验表空间第一个数据页的正确性(<code>fil_check_first_page</code>)，表空间无法访问也继续做崩溃恢复(<code>fil_open_single_table_tablespace</code>、<code>fil_load_single_table_tablespace</code>)，ddl操作不能进行(<code>check_if_supported_inplace_alter</code>)，同时数据库也被不能进行写入操作(<code>row_insert_for_mysql</code>、<code>row_update_for_mysql</code>等)，所有的prepare事务也会被回滚(<code>trx_resurrect_insert</code>、<code>trx_resurrect_update_in_prepared_state</code>)。这个选项还是很常用的，数据页可能是因为磁盘坏了而损坏了，设置为1，能保证数据库正常启动。
innodb_force_recovery = 2。除了设置1之后的操作不会运行，后台的master和purge线程就不会启动了(<code>srv_master_thread</code>、<code>srv_purge_coordinator_thread</code>等)，当你发现数据库因为这两个线程的原因而无法启动时，可以设置。
innodb_force_recovery = 3。除了设置2之后的操作不会运行，undo回滚数据库也不会进行，但是回滚段依然会被扫描，undo链表也依然会被创建(<code>trx_sys_init_at_db_start</code>)。srv_read_only_mode会被打开。
innodb_force_recovery = 4。除了设置3之后的操作不会运行，ibuf的操作也不会运行(<code>ibuf_merge_or_delete_for_page</code>)，表信息统计的线程也不会运行(因为一个坏的索引页会导致数据库崩溃)(<code>info_low</code>、<code>dict_stats_update</code>等)。从这个选项开始，之后的所有选项，都会损坏数据，慎重使用。
innodb_force_recovery = 5。除了设置4之后的操作不会运行，回滚段也不会被扫描(<code>recv_recovery_rollback_active</code>)，undo链表也不会被创建，这个主要用在undo日志被写坏的情况下。
innodb_force_recovery = 6。除了设置5之后的操作不会运行，数据库前滚操作也不会进行，包括解析和应用(<code>recv_recovery_from_checkpoint_start_func</code>)。</p>
<h2>总结</h2>
<p>InnoDB实现了一套完善的崩溃恢复机制，保证在任何状态下(包括在崩溃恢复状态下)数据库挂了，都能正常恢复，这个是与文件系统最大的差别。此外，崩溃恢复通过redo日志这种物理日志来应用数据页的方法，给MySQL Replication带来了新的思路，备库是否可以通过类似应用redo日志的方式来同步数据呢？阿里云RDS MySQL团队在后续的产品中，给大家带来了类似的特性，敬请期待。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;数据页解析.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;临时表那些事儿.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4362e32f45645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
