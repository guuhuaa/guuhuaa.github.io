<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL · 引擎特性 · InnoDB 数据页解析.md</title>
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

                    <a class="current-tab" href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;数据页解析.md">MySQL · 引擎特性 · InnoDB 数据页解析.md</a>
                    

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
                        <div><h1>MySQL · 引擎特性 · InnoDB 数据页解析</h1>
<h2>前言</h2>
<p>之前介绍的[MySQL · 引擎特性 · InnoDB Buffer Pool](MySQL · 引擎特性 · InnoDB Buffer Pool.md)中，详细介绍了InnoDB Buffer Pool的实现细节，Buffer Pool主要就是用来存储数据页的，是数据页在内存中的动态存储方式，而本文介绍一下数据页在磁盘上的静态存储方式以及相关的操作。由于数据页的结构涉及InnoDB非常底层的代码，因此各个版本的MySQL都可以参考。相关代码主要集中在page目录下。</p>
<h2>基础知识</h2>
<p>数据库采用数据页的形式组织数据。MySQL默认的非压缩数据页为16KB。在ibd中间中，0-16KB偏移量即为0号数据页，16KB-32KB的为1号数据页，依次类推。数据页的头尾除了一些元信息外，还有Checksum校验值，这些校验值在写入磁盘前计算得到，当从磁盘中读取时，重新计算校验值并与数据页中存储的对比，如果发现不同，则会导致MySQL crash。遇到这种情况，往往需要从备份集中恢复数据，如果备份不可用，只能使用<code>innodb_force_recovery</code>强行启动，然后尽可能多的导出数据。这篇<a href="http://mysql.taobao.org/monthly/2017/11/01/">月报</a>中介绍了一种从物理文件中恢复数据的方法，在走投无路的情况下可以使用。</p>
<h2>数据页格式</h2>
<p>严格来讲，InnoDB的数据页有很多种，比如，索引页，Undo页，Inode页，系统页，BloB页等，一共有10多种。本文主要介绍最常见的索引页。下文中，没有特殊说明，数据页都指索引页。
数据页包括七个部分，数据页文件头，数据页头，最大最小记录，用户记录，空闲空间，数据目录，数据页尾部。
简单的来说，数据页分两部分，一部分存储数据记录，按照记录的大小通过记录的指针连接起来。另外一部分存储数据页的目录，用来加速查找。注意这个目录是稀疏的，即不是所有的记录在目录都有索引，平均是每隔六个记录才有一个目录。数据记录部分是从低地址向高地址空间增长的，而数据目录部分则相反。这种数据结构可以保证比较高的插入删除和查找效率。具体方法详见<code>核心函数</code>小节。
这篇<a href="http://mysql.taobao.org/monthly/2017/11/01/">月报</a>的最后有一张图，详细展示了数据页的结构，读者可以先自行了解一下，接下来，本文解释一下各个部分的内容。</p>
<h3>数据页文件头(Fil Header)</h3>
<p>这个部分主要用来存储表空间相关的信息。主要在fil0fil.h这个文件中。</p>
<p><code>FIL_PAGE_SPACE_OR_CHKSUM:</code> 这个占用四字节，主要用来存储数据页的checksum。注意，计算校验值的时候，并不是整个数据页都计算，有几个地方是不计算进去的(<code>buf_calc_page_crc32</code>和<code>buf_calc_page_new_checksum</code>)，例如头尾存checksum的地方，存space_id的地方(历史原因导致)。Checksum的计算方式详见<code>数据页Corruption</code>这一小节。
<code>FIL_PAGE_OFFSET:</code> 这个就是对应数据页的page number，每个表空间从0开始，即这个值乘以数据页的大小就可以得到数据页在文件中的起始偏移量。<code>fio_io</code>函数读取以及写入数据页的时候依赖这个规则。
<code>FIL_PAGE_PREV,FIL_PAGE_NEXT:</code> 这两个是指针，分别指向前一个数据页和后一个数据页。注意，这里的前后是指按照用户记录排序的先后顺序，也是逻辑顺序。因为在InnoDB数据页不断的分配和释放中，会导致逻辑上连续的数据页在物理上不连续。所以需要指针链接。前后两个指针共同构建了一个双向链表。
<code>FIL_PAGE_LSN:</code> 当前数据页最新被修改的lsn。这个字段非常重要，InnoDB redolog幂等的特性就依赖此字段。在奔溃恢复应用日志阶段，如果发现redolog的lsn小于等于这个值，就不需要再次应用redolog了。
<code>FIL_PAGE_TYPE:</code> 当前页面是哪种类型的数据页。包括，索引页，Undo页，Inode页，系统页，BloB页等十几种。
<code>FIL_PAGE_FILE_FLUSH_LSN:</code> ibdata文件第一个数据页才有意义，记录ibdata成功刷到磁盘的lsn。
<code>FIL_PAGE_ARCH_LOG_NO_OR_SPACE_ID:</code> 现在的版本就是用来存spaceid的。</p>
<h3>数据页头(Page Header)</h3>
<p>从存储的信息来看，这部分才是存的数据页相关的元信息。定义在page0page.h中。</p>
<p><code>PAGE_N_DIR_SLOTS:</code> 这个表示数据页中数据目录的个数。一个新建的空数据页，就有2个目录，分别指向最大记录和最小记录。在一个非空的数据页中，第一个目录永远指向最小记录，最后一个目录永远指向最大记录。当增加目录的时候，会递增这个值。
PAGE_HEAP_TOP: 这个指向数据页中的空闲空间的起始地址。大于这个地址的且小于数据目录的空间都是未分配的，可以被后续使用。但是由于空闲记录链表(<code>PAGE_FREE</code>)的存在，小于这个地址的也可能被重用。
PAGE_N_HEAP: 目前已经被使用空间中的记录数量，包括正常的记录和已经被删除(放入<code>PAGE_FREE</code>中)的记录。从代码逻辑看，这个值是不会减少的，每次都空闲空间记录的时候就会增加。在创建新的空页时候，默认被置为2，即最大和最小记录。此外，最高位被用来标记这个数据页是否存了新格式的记录(compact和redundant)。
<code>PAGE_FREE:</code> 删除记录的链表，记录被删除，会放到这个链表头上，如果这个页上有记录要插入，可以先从这里分配空间，如果空间不够，才从空闲地址(<code>PAGE_HEAP_TOP</code>)分配。注意放到这个链表里面的，都是被purge线程彻底删除的记录，delete-marked的记录不在这里。
<code>PAGE_GARBAGE:</code> 所有已经被删除的记录占用空间的大小。主要是为了方便计算空闲的空间。
<code>PAGE_LAST_INSERT:</code> 指向最近一个被插入的记录的。主要用来加速后续插入操作。
<code>PAGE_DIRECTION:</code> 最后一个记录插入的方向，目前就两个方向，从左边插入和从右边插入。也是用来加速后续插入操作。
<code>PAGE_N_DIRECTION:</code> 同一个方法插入的记录数。主要用来加速后续插入操作。
<code>PAGE_N_RECS:</code> 当前数据页中用户的记录，不包括最大和最小记录。与<code>PAGE_N_HEAP</code>不同，如果记录被标记为delete-marked，这个值就会递减。
<code>PAGE_MAX_TRX_ID:</code> 修改此数据页的当前最大事务id。
<code>PAGE_LEVEL:</code> 这个页是否是B树中的叶子节点。如果是0，就是叶子节点。
<code>PAGE_INDEX_ID:</code> 索引页的索引id。
<code>PAGE_BTR_SEG_LEAF,PAGE_BTR_SEG_TOP:</code> 分别是叶子节点和非叶子节点的段头页地址。</p>
<h3>最大最小记录(Infimum and Supremum Records)</h3>
<p>最大记录是这个数据页中逻辑上最大的记录，所有用户的记录都小于它。最小记录是数据页上最小的记录，所有用户记录都大于它。他们在数据页被创建的时候创建，而且不能被删除。引入他们主要是方便页内操作。</p>
<h3>用户记录(User Records)</h3>
<p>用户所有插入的记录都存放在这里，默认情况下记录跟记录之间没有间隙，但是如果重用了已删除记录的空间，就会导致空间碎片。每个记录都有指向下一个记录的指针，但是没有指向上一个记录的指针。记录按照主键顺序排序。即，用户可以从数据页最小记录开始遍历，直到最大的记录，这包括了所有正常的记录和所有被delete-marked记录，但是不会访问到被删除的记录(<code>PAGE_FREE</code>)。</p>
<h3>空闲空间(Free Space)</h3>
<p>从<code>PAGE_HEAP_TOP</code>开始，到最后一个数据目录，这之间的空间就是空闲空间，都被重置为0，当用户需要插入记录时候，首先在被删除的记录的空间中查找，如果没有找到合适的空间，就从这里分配。空间分配给记录后，需要递增<code>PAGE_N_RECS</code>和<code>PAGE_N_HEAP</code>。</p>
<h3>数据目录(Page Directory)</h3>
<p>用户的记录是从低地址向高地址扩展，而数据目录则相反。在数据页被初始化的时候，就会数据页最后(当然在checksum之前)创建两个数据目录，分别指向最大和最小记录。之后插入新的数据的时候，需要维护这个目录，例如必要的时候增加目录的个数。每个数据目录占用两个字节，存储对应记录的页内偏移量。假设目录N，这个目录N管理目录N-1(不包括)和目录N之间的记录，我们称目录N own 这些记录。在目录N指向的记录中，会有字段记录own记录的数量。由此可见，目录own的记录不能太多，因为太多的话，即意味着目录太过稀疏，不能很好的提高查询效率，但同时也不能own太少，这会导致目录数量变多，占用过多的空间。在InnoDB的实现中，目录own的记录数量在4-8之间，包括4和8，平均是6个记录。如果超过这个数量，就需要重新均衡目录的数量。目录的增加和删除可能需要进行内存拷贝，但是由于目录占用的总体空间很小，开销可以忽略不计。</p>
<h3>数据页尾部(Fil Trailer)</h3>
<p>这个部分处于数据页最后的位置，只有8个字节。低地址的四个字节存储checksum的值，高地址的四个字节存储FIL_PAGE_LSN的低位四字节。注意这里的checksum的值不一定与FIL_PAGE_SPACE_OR_CHKSUM的相同，这个依赖不同的checksum计算方法。</p>
<h2>核心函数</h2>
<p>本节详细剖析一下数据页相关的几个核心函数。</p>
<h3>插入记录</h3>
<p>核心入口函数在<code>page_cur_insert_rec_low</code>。核心步骤如下:</p>
<ol>
<li>获取记录的长度。函数传入参数就有已经组合好的完整记录，所以只需要从记录的元数据中获取即可。</li>
<li>首先从<code>PAGE_FREE</code>链表中尝试获取足够的空间。仅仅比较链表头的一个记录，如果这个记录的空间大于需要插入的记录的空间，则复用这块空间(包括heap_no)，否则就从<code>PAGE_HEAP_TOP</code>分配空间。如果这两个地方都没有，则返回空。这里注意一下，由于只判断Free链表的第一个头元素，所以算法对空间的利用率不是很高，估计也是为了操作方便。假设，某个数据页首先删除了几条大的记录，但是最后一条删除的是比较小的记录A，那么后续插入的记录大小只有比记录A还小，才能把Free链表利用起来。举个例子，假设先后删除记录的大小为4K, 3K, 5K, 2K，那么只有当插入的记录小于2K时候，这些被删除的空间才会被利用起来，假设新插入的记录是0.5K，那么Free链表头的2K，可以被重用，但是只是用了前面的0.5K，剩下的1.5K依然会被浪费，下次插入只能利用5K记录所占的空间，并不会把剩下的1.5K也利用起来。这些特性，从底层解释了，为什么InnoDB那么容易产生碎片，经常需要进行空间整理。</li>
<li>如果Free链表不够，就从<code>PAGE_HEAP_TOP</code>分配，如果分配成功，需要递增<code>PAGE_N_HEAP</code>。</li>
<li>如果这个数据页有足够的空间，则拷贝记录到指定的空间。</li>
<li>修改新插入记录前驱上的next指针，同时修改这条新插入记录的指针next指针。这两步主要是保证记录上链表的连续性。</li>
<li>递增<code>PAGE_N_RECS</code>。设置heap_no。设置owned值为0。</li>
<li>更新<code>PAGE_LAST_INSERT</code>，<code>PAGE_DIRECTION</code>，<code>PAGE_N_DIRECTION</code>，设置这些参数后，可以一定程度上提高连续插入的性能，因为插入前需要先定位插入的位置，有了这些信息可以加快查找。详见查找记录代码分析。</li>
<li>修改数据目录。因为增加了一条新的记录，可能有些目录own的记录数量超过了最大值(目前是8条)，需要重新整理一下这个数据页的目录(<code>page_dir_split_slot</code>)。算法比较简单，就是找到中间节点，然后用这个中间节点重新构建一个新的目录，为了给这个新的目录腾空间，需要把后续的所有目录都平移，这个涉及一次momove操作(<code>page_dir_split_slot</code>和<code>page_dir_add_slot</code>)。</li>
<li>写redolog日志，持久化操作。</li>
<li>如果有blob字段，则处理独立的off-page。</li>
</ol>
<h3>删除记录</h3>
<p>注意这里的删除操作是指真正的删除物理记录，而不是标记记录为delete-mark。核心函数入口函数在<code>page_cur_delete_rec</code>。步骤如下：</p>
<ol>
<li>如果需要删除的记录是这个数据页的最后一个记录，那么直接把这个数据页重新初始化成空页(<code>page_create_empty</code>)即可。</li>
<li>如果不是最后一条，就走正常路径。首先记录redolog日志。</li>
<li>重置<code>PAGE_LAST_INSERT</code>和递增block的modify clock。后者主要是为了让乐观的查询失效。</li>
<li>找到需要删除记录的前驱和后继记录，然后修改指针，使前驱直接指向后继。这样记录的链表上就没有这条记录了。</li>
<li>如果一个目录指向这条被删除的记录，那么让这个目录指向删除记录的前驱，同时减少这个目录own的记录数。</li>
<li>如果这个记录有blob的off-page，则删除。</li>
<li>把记录放到<code>PAGE_FREE</code>链表头部，然后递增<code>PAGE_GARBAGE</code>的大小，减小<code>PAGE_N_RECS</code>用户记录的值。</li>
<li>由于第五步中递减了own值，可能导致own的记录数小于最小值(目前是4条)。所以需要重新均衡目录，可能需要删除某些目录(<code>page_dir_balance_slot</code>)。具体算法也比较简单，首先判断是否可以从周围的目录中挪一条记录过来，如果可以直接调整一下前后目录的指针即可。这种简单的调整要求被挪出记录的目录own的记录数量足够多，如果也没有足够的记录，就需要删除其中一个目录，然后把后面的目录都向前平移(<code>page_dir_delete_slot</code>)。</li>
</ol>
<h3>查找记录/定位位置</h3>
<p>在InnoDB中，需要查找某条件记录，需要调用函数page_cur_search_with_match，但如果需要定位某个位置，例如大于某条记录的第一条记录，也需要使用同一个函数。定位的位置有PAGE_CUR_G，PAGE_CUR_GE，PAGE_CUR_L，PAGE_CUR_LE四种，分别表示大于，大于等于，小于，小于等于四种位置。
由于数据页目录的存在，查找和定位就相对简单，先用二分查找，定位周边的两个目录，然后再用线性查找的方式定位最终的记录或者位置。
此外，由于每次插入前，都需要调用这个函数确定插入位置，为了提高效率，InnoDB针对按照主键顺序插入的场景做了一个小小的优化。因为如果按照主键顺序插入的话，能保证每次都插入在这个数据页的最后，所以只需要直接把位置直接定位在数据页的最后(<code>PAGE_LAST_INSERT</code>)就可以了。至于怎么判断当前是否按照主键顺序插入，就依赖<code>PAGE_N_DIRECTION</code>，<code>PAGE_LAST_INSERT</code>，<code>PAGE_DIRECTION</code>这几个信息了，目前的代码中要求满足5个条件：</p>
<ol>
<li>当前的数据页是叶子节点</li>
<li>位置查询模式为PAGE_CUR_LE</li>
<li>相同方向的插入已经大于3了(<code>page_header_get_field(page, PAGE_N_DIRECTION) &gt; 3</code>)</li>
<li>最后插入的记录的偏移量为空(<code>page_header_get_ptr(page, PAGE_LAST_INSERT) != 0</code>)</li>
<li>从右边插入的(<code>page_header_get_field(page, PAGE_DIRECTION) == PAGE_RIGHT</code>)</li>
</ol>
<h3>其他函数</h3>
<p>除了插入删除查找外，还有一些函数也比较重要，例如：
<code>page_create</code>，创建新的空页的时候，都需要调用这个函数来初始化元信息。
<code>page_move_rec_list_end</code>，当数据页需要重组时候，需要把数据从一个数据页拷贝到另外一个，这个时候就需要用到。类似的还有函数<code>page_move_rec_list_start</code>，两个函数的拷贝方式不同，一个是从头开始拷贝到指定的记录，另外一个是从指定记录开始拷贝到数据页最后。
<code>page_validate</code>，这种函数主要是debug模式下校验数据页是否损坏的检验函数，不做什么实际工作，但是这些函数非常时候初学者阅读，能快读的理解数据页的结构。
<code>page_cur_open_on_rnd_user_rec</code>，这函数是把位置放到一个随机的记录上，当change buffer的B树满的时候，目前的逻辑是随机选一条记录，进行合并。</p>
<h2>数据页Corruption</h2>
<p>数据页的checksum值的计算方法依赖参数<code>innodb_checksum_algorithm</code>。目前提供三种计算checksum的方法，第一种是crc校验(<code>buf_calc_page_crc32</code>)，这种是一种比较新的计算方法，但是可以使用cpu硬件指令来加速。第二种是innodb校验，是innodb自己开发的一种计算方法，但是有新老两种变体，两种变体计算结果不同，为了兼容老的变体，需要在代码中兼容。第三种是none模式，这种计算方式不计算每个数据页的校验值，而是使用一个指定的值填充checksum字段，这种方式速度很快，但也保证不了数据的正确性。在<code>innodb_checksum_algorithm</code>中，除了innodb,crc32,none三种选项之外，还有strict带头的选项。strict的选项表示，在读取的时候必须是指定的校验方式的校验值才通过，其他的都不行，例如，指定了strict_crc32，那么在数据页被读取计算checksum时候，对应的校验值必须也是crc32的才可通过，但是如果指定crc32，如果存储的是innodb或者none的结果，也是可以通过校验的。之所以提供了这种选项，就是为了兼容老版本的mysql以及防止校验算法被修改而导致的数据不可用。这里提醒一下，使用strict模式由于计算量比较小，因此效率相对较高。</p>
<p>接下里，分析一下checksum写入和读取校验的代码细节。
在一个数据页即将被刷入磁盘的时候，会调用函数<code>buf_flush_init_for_writing</code>进行相关元信息的修改。这里主要包括newest_len和checksum。函数中首先往<code>FIL_PAGE_LSN</code>和<code>UNIV_PAGE_SIZE - FIL_PAGE_END_LSN_OLD_CHKSUM</code>分别写入8个字节的newest_lsn，接着计算checksum，填入<code>FIL_PAGE_SPACE_OR_CHKSUM</code>，同时覆盖<code>UNIV_PAGE_SIZE - FIL_PAGE_END_LSN_OLD_CHKSUM</code>起始的四个字节。我们会发现，如果算法是crc32或者none，那么前后两个checksum存储的内容相同，如果是innodb，则后面的checksum会存老版的值。
在一个数据页从磁盘读取的时候，IO线程会回调<code>buf_page_io_complete</code>函数，如果是读取操作，这个函数中会调用函数<code>buf_page_is_corrupted</code>校验数据页的正确性。<code>buf_page_is_corrupted</code>首先会校验头尾的newest_lsn的低四字节是否相同(<code>FIL_PAGE_LSN</code>+4和<code>UNIV_PAGE_SIZE- FIL_PAGE_END_LSN_OLD_CHKSUM</code>+4)，如果不相同，直接认为数据页损坏了。接下里会把完整的8字节lsn读取出来，跟系统当前的lsn对比，如果比当前的大，也认为数据页坏了。接下里，会把首尾的checksum都读取出来，如果发现都为0，则进一步判断是否是空页，如果是空页，则认为这个数据页正常(可能是extend文件出来的空页)。接下来，计算数据页内容的校验值，与存储在数据页首尾的值进行比较。在strict算法下，必须完全一致才认为数据页完整，在非strict模式下，只要有一种值匹配即可了。如果校验值通过，则认为数据页完好。如果数据页损坏，则会调用函数<code>buf_page_print</code>输出数据页的信息至错误日志，这也是我们常常看到的数据页错误日志。这个函数会把数据页所有内容，space_id，page_no，头尾lsn，头尾checksum以及各种算法计算的checksum都打印出来，此外，还会依据<code>FIL_PAGE_TYPE</code>推测可能的数据页种类，方便排查问题。</p>
<h2>总结</h2>
<p>总体来说，InnoDB数据页的结构设计折中了插入，删除以及查找的效率，是一种值得学习的数据结构。此外，了解其的结构和原理，当数据页发生损坏的时候，能不慌不忙，尽最大的努力找出残存的数据，这也是一个优秀DBA不可缺少的素质。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;同步机制.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB崩溃恢复.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4362d3b954645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
