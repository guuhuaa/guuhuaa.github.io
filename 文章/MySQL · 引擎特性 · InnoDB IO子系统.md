<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL · 引擎特性 · InnoDB IO子系统.md</title>
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

                    <a class="current-tab" href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;IO子系统.md">MySQL · 引擎特性 · InnoDB IO子系统.md</a>
                    

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
                        <div><h1>MySQL · 引擎特性 · InnoDB IO子系统</h1>
<h2>前言</h2>
<p>InnoDB做为一款成熟的跨平台数据库引擎，其实现了一套高效易用的IO接口，包括同步异步IO，IO合并等。本文简单介绍一下其内部实现，主要的代码集中在os0file.cc这个文件中。本文的分析默认基于MySQL 5.6，CentOS 6，gcc 4.8，其他版本的信息会另行指出。</p>
<h2>基础知识</h2>
<p><em><strong>WAL技术 :</strong></em> 日志先行技术，基本所有的数据库，都使用了这个技术。简单的说，就是需要写数据块的时候，数据库前台线程把对应的日志先写（批量顺序写）到磁盘上，然后就告诉客户端操作成功，至于真正写数据块的操作（离散随机写）则放到后台IO线程中。使用了这个技术，虽然多了一个磁盘写入操作，但是由于日志是批量顺序写，效率很高，所以客户端很快就能得到相应。此外，如果在真正的数据块落盘之前，数据库奔溃，重启时候，数据库可以使用日志来做崩溃恢复，不会导致数据丢失。
<em><strong>数据预读 :</strong></em> 与数据块A“相邻”的数据块B和C在A被读取的时候，B和C也会有很大的概率被读取，所以可以在读取B的时候，提前把他们读到内存中，这就是数据预读技术。这里说的相邻有两种含义，一种是物理上的相邻，一种是逻辑上的相邻。底层数据文件中相邻，叫做物理上相邻。如果数据文件中不相邻，但是逻辑上相邻（id=1的数据和id=2的数据，逻辑上相邻，但是物理上不一定相邻，可能存在同一个文件中不同的位置），则叫逻辑相邻。
<em><strong>文件打开模式 :</strong></em> Open系统调用常见的模式主要三种：O_DIRECT，O_SYNC以及default模式。O_DIRECT模式表示后续对文件的操作不使用文件系统的缓存，用户态直接操作设备文件，绕过了内核的缓存和优化，从另外一个角度来说，使用O_DIRECT模式进行写文件，如果返回成功，数据就真的落盘了（不考虑磁盘自带的缓存），使用O_DIRECT模式进行读文件，每次读操作是真的从磁盘中读取，不会从文件系统的缓存中读取。O_SYNC表示使用操作系统缓存，对文件的读写都经过内核，但是这个模式还保证每次写数据后，数据一定落盘。default模式与O_SYNC模式类似，只是写数据后不保证数据一定落盘，数据有可能还在文件系统中，当主机宕机，数据有可能丢失。
此外，写操作不仅需要修改或者增加的数据落盘，而且还需要文件元信息落盘，只有两部分都落盘了，才能保证数据不丢。O_DIRECT模式不保证文件元信息落盘(但大部分文件系统都保证，Bug #45892)，因此如果不做其他操作，用O_DIRECT写文件后，也存在丢失的风险。O_SYNC则保证数据和元信息都落盘。default模式两种数据都不保证。
调用函数fsync后，能保证数据和日志都落盘，因此使用O_DIRECT和default模式打开的文件，写完数据，需要调用fsync函数。
<em><strong>同步IO :</strong></em> 我们常用的read/write函数（Linux上）就是这类IO，特点是，在函数执行的时候，调用者会等待函数执行完成，而且没有消息通知机制，因为函数返回了，就表示操作完成了，后续直接检查返回值就可知道操作是否成功。这类IO操作，编程比较简单，在同一个线程中就能完成所有操作，但是需要调用者等待，在数据库系统中，比较适合急需某些数据的时候调用，例如WAL中日志必须在返回客户端前落盘，则进行一次同步IO操作。
<em><strong>异步IO :</strong></em> 在数据库中，后台刷数据块的IO线程，基本都使用了异步IO。数据库前台线程只需要把刷块请求提交到异步IO的队列中即可返回做其他事情，而后台线程IO线程，则定期检查这些提交的请求是否已经完成，如果完成再做一些后续处理工作。同时异步IO由于常常是一批一批的请求提交，如果不同请求访问同一个文件且偏移量连续，则可以合并成一个IO请求。例如，第一个请求读取文件1，偏移量100开始的200字节数据，第二个请求读取文件1，偏移量300开始的100字节数据，则这两个请求可以合并为读取文件1，偏移量100开始的300字节数据。数据预读中的逻辑预读也常常使用异步IO技术。
目前Linux上的异步IO库，需要文件使用O_DIRECT模式打开，且数据块存放的内存地址、文件读写的偏移量和读写的数据量必须是文件系统逻辑块大小的整数倍，文件系统逻辑块大小可以使用类似<code>sudo blockdev --getss /dev/sda5</code>的语句查询。如果上述三者不是文件系统逻辑块大小的整数倍，则在调用读写函数时候会报错EINVAL，但是如果文件不使用O_DIRECT打开，则程序依然可以运行，只是退化成同步IO，阻塞在io_submit函数调用上。</p>
<h2>InnoDB常规IO操作以及同步IO</h2>
<p>在InnoDB中，如果系统有pread/pwrite函数(<code>os_file_read_func</code>和<code>os_file_write_func</code>)，则使用它们进行读写，否则使用lseek+read/write方案。这个就是InnoDB同步IO。查看pread/pwrite文档可知，这两个函数不会改变文件句柄的偏移量且线程安全，所以多线程环境下推荐使用，而lseek+read/write方案则需要自己使用互斥锁保护，在高并发情况下，频繁的陷入内核态，对性能有一定影响。</p>
<p>在InnoDB中，使用open系统调用打开文件(<code>os_file_create_func</code>)，模式方面除了O_RDONLY(只读)，O_RDWR(读写)，O_CREAT(创建文件)外，还使用了O_EXCL(保证是这个线程创建此文件)和O_TRUNC(清空文件)。默认情况下(数据库不设置为只读模式)，所有文件都以O_RDWR模式打开。innodb_flush_method这个参数比较重要，重点介绍一下：</p>
<ul>
<li>如果innodb_flush_method设置了O_DSYNC，日志文件(ib_logfileXXX)使用O_SYNC打开，因此写完数据不需要调用函数fsync刷盘，数据文件(ibd)使用default模式打开，因此写完数据需要调用fsync刷盘。</li>
<li>如果innodb_flush_method设置了O_DIRECT，日志文件(ib_logfileXXX)使用default模式打开，写完数据需要调用fsync函数刷盘，数据文件(ibd)使用O_DIRECT模式打开，写完数据需要调用fsync函数刷盘。</li>
<li>如果innodb_flush_method设置了fsync或者不设置，数据文件和日志文件都使用default模式打开，写完数据都需要使用fsync来刷盘。</li>
<li>如果innodb_flush_method设置为O_DIRECT_NO_FSYNC，文件打开方式与O_DIRECT模式类似，区别是，数据文件写完后，不调用fsync函数来刷盘，主要针对O_DIRECT能保证文件的元数据也落盘的文件系统。
InnoDB目前还不支持使用O_DIRECT模式打开日志文件，也不支持使用O_SYNC模式打开数据文件。
注意，如果使用linux native aio（详见下一节），innodb_flush_method一定要配置成O_DIRECT，否则会退化成同步IO（错误日志中不会有任务提示）。</li>
</ul>
<p>InnoDB使用了文件系统的文件锁来保证只有一个进程对某个文件进行读写操作(<code>os_file_lock</code>)，使用了建议锁(Advisory locking)，而不是强制锁(Mandatory locking)，因为强制锁在不少系统上有bug，包括linux。在非只读模式下，所有文件打开后，都用文件锁锁住。</p>
<p>InnoDB中目录的创建使用递归的方式(<code>os_file_create_subdirs_if_needed</code>和<code>os_file_create_directory</code>)。例如，需要创建/a/b/c/这个目录，先创建c，然后b，然后a，创建目录调用mkdir函数。此外，创建目录上层需要调用<code>os_file_create_simple_func</code>函数，而不是<code>os_file_create_func</code>，需要注意一下。</p>
<p>InnoDB也需要临时文件，临时文件的创建逻辑比较简单(<code>os_file_create_tmpfile</code>)，就是在tmp目录下成功创建一个文件后直接使用unlink函数释放掉句柄，这样当进程结束后(不管是正常结束还是异常结束)，这个文件都会自动释放。InnoDB创建临时文件，首先复用了server层函数mysql_tmpfile的逻辑，后续由于需要调用server层的函数来释放资源，其又调用dup函数拷贝了一份句柄。</p>
<p>如果需要获取某个文件的大小，InnoDB并不是去查文件的元数据(<code>stat</code>函数)，而是使用<code>lseek(file, 0, SEEK_END)</code>的方式获取文件大小，这样做的原因是防止元信息更新延迟导致获取的文件大小有误。</p>
<p>InnoDB会预分配一个大小给所有新建的文件(包括数据和日志文件)，预分配的文件内容全部置为零(<code>os_file_set_size</code>)，当前文件被写满时，再进行扩展。此外，在日志文件创建时，即install_db阶段，会以100MB的间隔在错误日志中输出分配进度。</p>
<p>总体来说，常规IO操作和同步IO相对比较简单，但是在InnoDB中，数据文件的写入基本都用了异步IO。</p>
<h2>InnoDB异步IO</h2>
<p>由于MySQL诞生在Linux native aio之前，所以在MySQL异步IO的代码中，有两种实现异步IO的方案。
第一种是原始的Simulated aio，InnoDB在Linux native air被import进来之前以及某些不支持air的系统上，自己模拟了一条aio的机制。异步读写请求提交时，仅仅把它放入一个队列中，然后就返回，程序可以去做其他事情。后台有若干异步io处理线程(innobase_read_io_threads和innobase_write_io_threads这两个参数控制)不断从这个队列中取出请求，然后使用同步IO的方式完成读写请求以及读写完成后的工作。
另外一种就是Native aio。目前在linux上使用io_submit，io_getevents等函数完成(不使用glibc aio，这个也是模拟的)。提交请求使用io_submit, 等待请求使用io_getevents。另外，window平台上也有自己对应的aio，这里就不介绍了，如果使用了window的技术栈，数据库应该会选用sqlserver。目前，其他平台(Linux和window之外)都只能使用Simulate aio。</p>
<p>首先介绍一下一些通用的函数和结构，接下来分别详细介绍一下Simulate alo和Linux上的Native aio。
在os0file.cc中定义了全局数组，类型为<code>os_aio_array_t</code>，这些数组就是Simulate aio用来缓存读写请求的队列，数组的每一个元素是<code>os_aio_slot_t</code>类型，里面记录了每个IO请求的类型，文件的fd，偏移量，需要读取的数据量，IO请求发起的时间，IO请求是否已经完成等。另外，Linux native io中的struct iocb也在<code>os_aio_slot_t</code>中。数组结构<code>os_aio_slot_t</code>中，记录了一些统计信息，例如有多少数据元素(<code>os_aio_slot_t</code>)已经被使用了，是否为空，是否为满等。这样的全局数组一共有5个，分别用来保存数据文件读异步请求(<code>os_aio_read_array</code>)，数据文件写异步请求(<code>os_aio_write_array</code>)，日志文件写异步请求(<code>os_aio_log_array</code>)，insert buffer写异步请求(<code>os_aio_ibuf_array</code>)，数据文件同步读写请求(<code>os_aio_sync_array</code>)。日志文件的数据块写入是同步IO，但是这里为什么还要给日志写分配一个异步请求队列(<code>os_aio_log_array</code>)呢？原因是，InnoDB日志文件的日志头中，需要记录checkpoint的信息，目前checkpoint信息的读写还是用异步IO来实现的，因为不是很紧急。在window平台中，如果对特定文件使用了异步IO，就这个文件就不能使用同步IO了，所以引入了数据文件同步读写请求队列(<code>os_aio_sync_array</code>)。日志文件不需要读异步请求队列，因为只有在做奔溃恢复的时候日志才需要被读取，而做崩溃恢复的时候，数据库还不可用，因此完全没必要搞成异步读取模式。这里有一点需要注意，不管变量innobase_read_io_threads和innobase_write_io_threads两个参数是多少，<code>os_aio_read_array</code>和<code>os_aio_write_array</code>都只有一个，只不过数据中的<code>os_aio_slot_t</code>元素会相应增加，在linux中，变量加1，元素数量增加256。例如，innobase_read_io_threads=4，则os_aio_read_array数组被分成了四部分，每一个部分256个元素，每个部分都有自己独立的锁、信号量以及统计变量，用来模拟4个线程，innobase_write_io_threads类似。从这里我们也可以看出，每个异步read/write线程能缓存的读写请求是有上限的，即为256，如果超过这个数，后续的异步请求需要等待。256可以理解为InnoDB层对异步IO并发数的控制，而在文件系统层和磁盘层面也有长度限制，分别使用<code>cat /sys/block/sda/queue/nr_requests</code>和<code>cat /sys/block/sdb/queue/nr_requests</code>查询。
<code>os_aio_init</code>在InnoDB启动的时候调用，用来初始化各种结构，包括上述的全局数组，还有Simulate aio中用的锁和互斥量。<code>os_aio_free</code>则释放相应的结构。<code>os_aio_print_XXX</code>系列的函数用来输出aio子系统的状态，主要用在<code>show engine innodb status</code>语句中。</p>
<h3>Simulate aio</h3>
<p>Simulate aio相对Native aio来说，由于InnoDB自己实现了一套模拟机制，相对比较复杂。</p>
<ul>
<li>入口函数为<code>os_aio_func</code>，在debug模式下，会校验一下参数，例如数据块存放的内存地址、文件读写的偏移量和读写的数据量是否是OS_FILE_LOG_BLOCK_SIZE的整数倍，但是没有检验文件打开模式是否用了O_DIRECT，因为Simulate aio最终都是使用同步IO，没有必要一定要用O_DIRECT打开文件。</li>
<li>校验通过后，就调用<code>os_aio_array_reserve_slot</code>，作用是把这个IO请求分配到某一个后台io处理线程(innobase_xxxx_io_threads分配的，但其实是在同一个全局数组中)中，并把io请求的相关信息记录下来，方便后台io线程处理。如果IO请求类型相同，请求同一个文件且偏移量比较接近(默认情况下，偏移量差别在1M内)，则InnoDB会把这两个请求分配到同一个io线程中，方便在后续步骤中IO合并。</li>
<li>提交IO请求后，需要唤醒后台io处理线程，因为如果后台线程检测到没有IO请求，会进入等待状态(<code>os_event_wait</code>)。</li>
<li>至此，函数返回，程序可以去干其他事情了，后续的IO处理交给后台线程了。
介绍一下后台IO线程怎么处理的。</li>
<li>InnoDB启动时，后台IO线程会被启动(<code>io_handler_thread</code>)。其会调用<code>os_aio_simulated_handle</code>从全局数组中取出IO请求，然后用同步IO处理，结束后，需要做收尾工作，例如，如果是写请求的话，则需要在buffer pool中把对应的数据页从脏页列表中移除。</li>
<li><code>os_aio_simulated_handle</code>首先需要从数组中挑选出某个IO请求来执行，挑选算法并不是简单的先进先出，其挑选所有请求中offset最小的请求先处理，这样做是为了后续的IO合并比较方便计算。但是这也容易导致某些offset特别大的孤立请求长时间没有被执行到，也就是饿死，为了解决这个问题，在挑选IO请求之前，InnoDB会先做一次遍历，如果发现有请求是2s前推送过来的(也就是等待了2s)，但是还没有被执行，就优先执行最老的请求，防止这些请求被饿死，如果有两个请求等待时间相同，则选择offset小的请求。</li>
<li><code>os_aio_simulated_handle</code>接下来要做的工作就是进行IO合并，例如，读请求1请求的是file1，offset100开始的200字节，读请求2请求的是file1，offset300开始的100字节，则这两个请求可以合并为一个请求：file1，offset100开始的300字节，IO返回后，再把数据拷贝到原始请求的buffer中就可以了。写请求也类似，在写操作之前先把需要写的数据拷贝到一个临时空间，然后一次写完。注意，只有在offset连续的情况下IO才会合并，有间断或者重叠都不会合并，一模一样的IO请求也不会合并，所以这里可以算是一个可优化的点。</li>
<li><code>os_aio_simulated_handle</code>如果发现现在没有IO请求，就会进入等待状态，等待被唤醒</li>
</ul>
<p>综上所述，可以看出IO请求是一个一个的push的对立面，每push进一个后台线程就拿去处理，如果后台线程优先级比较高的话，IO合并效果可能比较差，为了解决这个问题，Simulate aio提供类似组提交的功能，即一组IO请求提交后，才唤醒后台线程，让其统一进行处理，这样IO合并的效果会比较好。但这个依然有点小问题，如果后台线程比较繁忙的话，其就不会进入等待状态，也就是说只要请求进入了队列，就会被处理。这个问题在下面的Native aio中可以解决。
总体来说，InnoDB实现的这一套模拟机制还是比较安全可靠的，如果平台不支持Native aio则使用这套机制来读写数据文件。</p>
<h3>Linux native aio</h3>
<p>如果系统安装了libaio库且在配置文件里面设置了innodb_use_native_aio=on则启动时候会使用Native aio。</p>
<ul>
<li>入口函数依然为<code>os_aio_func</code>，在debug模式下，依然会检查传入的参数，同样不会检查文件是否以O_DIRECT模式打开，这算是一个有点风险的点，如果用户不知道linux native aio需要使用O_DIRECT模式打开文件才能发挥出aio的优势，那么性能就不会达到预期。建议在此处做一下检查，有问题输出到错误日志。</li>
<li>检查通过之后，与Simulated aio一样，调用<code>os_aio_array_reserve_slot</code>，把IO请求分配给后台线程，分配算法也考虑了后续的IO合并，与Simulated aio一样。不同之处，主要是需要用IO请求的参数初始化iocb这个结构。IO请求的相关信息除了需要初始化iocb外，也需要在全局数组的slot中记录一份，主要是为了在<code>os_aio_print_XXX</code>系列函数中统计方便。</li>
<li>调用io_submit提交请求。</li>
<li>至此，函数返回，程序可以去干其他事情了，后续的IO处理交给后台线程了。
接下来是后台IO线程。</li>
<li>与Simulate aio类似，后台IO线程也是在InnoDB启动时候启动。如果是Linux native aio，后续会调用<code>os_aio_linux_handle</code>这个函数。这个函数的作用与<code>os_aio_simulated_handle</code>类似，但是底层实现相对比较简单，其仅仅调用io_getevents函数等待IO请求完成。超时时间为0.5s，也就是说如果即使0.5内没有IO请求完成，函数也会返回，继续调用io_getevents等待，当然在等待前会判断一下服务器是否处于关闭状态，如果是则退出。</li>
</ul>
<p>在分发IO线程时，尽量把相邻的IO放在一个线程内，这个与Simulate aio类似，但是后续的IO合并操作，Simulate aio是自己实现，Native aio则交给内核完成了，因此代码比较简单。
还要一个区别是，当没有IO请求的时候，Simulate aio会进入等待状态，而Native aio则会每0.5秒醒来一次，做一些检查工作，然后继续等待。因此，当有新的请求来时，Simulated aio需要用户线程唤醒，而Native aio不需要。此外，在服务器关闭时，Simulate aio也需要唤醒，Native aio则不需要。</p>
<p>可以发现，Native aio与Simulate aio类似，请求也是一个一个提交，然后一个一个处理，这样会导致IO合并效果比较差。Facebook团队提交了一个Native aio的组提交优化：把IO请求首先缓存，等IO请求都到了之后，再调用io_submit函数，一口气提交先前的所有请求(io_submit可以一次提交多个请求)，这样内核就比较方便做IO优化。Simulate aio在IO线程压力大的情况下，组提交优化会失效，而Native aio则不会。注意，组提交优化，不能一口气提交太多，如果超过了aio等待队列长度，会强制发起一次io_submit。</p>
<h2>总结</h2>
<p>本文详细介绍了InnoDB中IO子系统的实现以及使用需要注意的点。InnoDB日志使用同步IO，数据使用异步IO，异步IO的写盘顺序也不是先进先出的模式，这些点都需要注意。Simulate aio虽然有比较大的学习价值，但是在现代操作系统中，推荐使用Native aio。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;Buffer&#32;Pool.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;事务系统.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4362bd7d9b645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
