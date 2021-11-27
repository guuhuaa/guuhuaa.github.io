<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL优化：优化 select count().md</title>
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

                    <a class="current-tab" href="MySQL优化：优化&#32;select&#32;count().md">MySQL优化：优化 select count().md</a>
                    

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
                        <div><h1>MySQL优化：优化 select count()</h1>
<h3>业务反馈，开发崩溃</h3>
<p>某天，项目中业务人员反馈系统中某功能查询非常的慢，几乎等待了几十秒才有反应。于是联系了开发，开发人员调取日志，排查应用，定位 SQL，其实只是一个 <code>select count(*)</code>，这可急坏了开发人员，非常困惑，最简答的一个统计 SQL，为什么查询这么慢！不知道到如何优化与处理。</p>
<p><strong>一个效果显著的简单操作</strong></p>
<p>在我知道这个问题，询问了开发人员哪张表后，做了一定分析后，<strong>增加索引</strong>，无需开发做任何修改，性能得到大幅提升。为什么一个索引会有如此的性能提升，我先卖个关子，后面一一道来。</p>
<h3>问题复现，优化处理</h3>
<p>首先我们造一个 500W 数据量的表，别结构如下：</p>
<pre><code>mysql&gt; show create table sbtest1\G;
*************************** 1. row ***************************
       Table: sbtest1
Create Table: CREATE TABLE `sbtest1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` int(11) NOT NULL DEFAULT '0',
  `c` char(120) NOT NULL DEFAULT '',
  `pad` char(60) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5000001 DEFAULT CHARSET=latin1
</code></pre>
<p>直接来 count(*) 一下，看看执行时间吧。</p>
<pre><code>mysql&gt; select count(*) from sbtest1;
+----------+
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (2.42 sec)
</code></pre>
<p>执行时间 2.42 秒。</p>
<p>现在看看执行计划：</p>
<pre><code>mysql&gt; explain select count(*) from sbtest1;
+----+-------------+---------+------------+-------+---------------+---------+---------+------+---------+----------+-------------+
| id | select_type | table   | partitions | type  | possible_keys | key     | key_len | ref  | rows    | filtered | Extra       |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+---------+----------+-------------+
|  1 | SIMPLE      | sbtest1 | NULL       | index | NULL          | PRIMARY | 4       | NULL | 4808163 |   100.00 | Using index |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+---------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
</code></pre>
<p><strong>结果显示：走 PRIMARY 索引。</strong></p>
<p>是不是有疑惑了，查询走了主键索引，看着没什么问题呀，500W 的数据 2 秒执行完，还可以。那你就错了，我这里只是一个简单的测试表，这才几个字段，测试表造的数据又是多么的简单，倘若在真实生产环境，这 500W 的数据可不是 2 秒就能返回结果的。</p>
<p>稍等片刻，我来优化……
……
……
……</p>
<pre><code>mysql&gt; select count(*) from sbtest1;
+----------+
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (0.68 sec)
</code></pre>
<p>执行时间明显缩短，我到底做了怎样的操作，为什么执行效率大幅提高，想知道其中的奥妙吗？干货即将送达。</p>
<h3>扒一扒 count(*) 的原理</h3>
<p>为了解开这其中的疑惑，首先我们不得不说一下 MySQL 的 count(*) 原理。</p>
<p>在 MySQL 中存在两种索引：</p>
<ul>
<li><strong>聚簇索引</strong>：MySQL 中的每个 InnoDB 存储引擎的表，都有一个特殊索引来保存每行记录，这个索引就是聚簇索引。通常情况下其实就是主键。聚簇索引保存的是行记录和 b-tree 索引，这个索引所占用的空间大小和行记录总数差不多大。</li>
<li><strong>二级索引</strong>：另外一类索引就是二级索引，它保存的只是本身索引列和主键列。占用的空间明显小很多了。</li>
</ul>
<p>介绍完 MySQL 的两种索引，我们继续说 MySQL 的 count(*) 执行过程。</p>
<p>在 MySQL 的 InnoDB 存储引擎中，count(*) 会从内存中读取数据到缓冲区中，如果内存中没有，会提前一步在磁盘中把数据读取到内存中，然后在缓存区中完成记录数的统计。MySQL 会先通过 ken_len 最小的那个二级索引计算，如果没有二级索引就通过主键计算，如果连主键都没有那就要通过全表扫描来完成计算了。</p>
<p>主键索引也就是聚簇索引，会把行记录和 b-tree 索引都读取出来，所占用的空间大小和行记录总数差不多大；二级索引保存的只是本身索引列和主键列，占用的空间会小的多，当然读取出来就节省了很多时间。</p>
<p>我举个通俗易懂的例子吧，比如学校给你一个任务，让你统计一下高三年级一共有多少学生？利用上面说的两种索引来统计。</p>
<ul>
<li>聚簇索引：从学号 1，一个一个数到 600，有 600 人。</li>
<li>二级索引：直接看学号 600，那不就是 600 人吗！</li>
</ul>
<p>通过这些就不难说明了，上述演示的过程，第一次是通过主键来计算统计数据量，而第二次其实我做的也是创建了一个二级索引，通过二级索引来计算统计，速度快了很多，我们可以看看其对应的执行过程。</p>
<pre><code>mysql&gt; explain select count(*) from sbtest1;
+----+-------------+---------+------------+-------+---------------+------+---------+------+---------+----------+-------------+
| id | select_type | table   | partitions | type  | possible_keys | key  | key_len | ref  | rows    | filtered | Extra       |
+----+-------------+---------+------------+-------+---------------+------+---------+------+---------+----------+-------------+
|  1 | SIMPLE      | sbtest1 | NULL       | index | NULL          | k_1  | 4       | NULL | 4808163 |   100.00 | Using index |
+----+-------------+---------+------------+-------+---------------+------+---------+------+---------+----------+-------------+
1 row in set, 1 warning (0.01 sec)
</code></pre>
<p>执行过程 key 这一列内容为：k_1，这个就是二级索引的索引名称。</p>
<h3>显而易见的验证</h3>
<h4>验证聚簇索引</h4>
<p>查询 MySQL 缓存区，确保缓冲区中不存在测试表的缓存：</p>
<pre><code>mysql&gt; select * from sys.innodb_buffer_stats_by_table where object_schema = 'sbtest';
Empty set (0.05 sec)
</code></pre>
<p>执行 <code>select count(*)</code>：</p>
<pre><code>mysql&gt; select count(*) from sbtest1;
+----------+
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (2.42 sec)
</code></pre>
<p>再次查看 MySQL 缓存区，查询测试表的缓存：</p>
<pre><code>mysql&gt; select * from sys.innodb_buffer_stats_by_table where object_schema = 'sbtest';
+---------------+-------------+------------+------------+-------+--------------+-----------+-------------+
| object_schema | object_name | allocated  | data       | pages | pages_hashed | pages_old | rows_cached |
+---------------+-------------+------------+------------+-------+--------------+-----------+-------------+
| sbtest        | sbtest1     | 125.84 MiB | 115.46 MiB |  8054 |            0 |      3021 |      588845 |
+---------------+-------------+------------+------------+-------+--------------+-----------+-------------+
1 row in set (0.13 sec)
</code></pre>
<p>结果显示：缓存了 100M+ 的数据。</p>
<p>查看执行计划：</p>
<pre><code>mysql&gt; explain select count(*) from sbtest1;
+----+-------------+---------+------------+-------+---------------+---------+---------+------+---------+----------+-------------+
| id | select_type | table   | partitions | type  | possible_keys | key     | key_len | ref  | rows    | filtered | Extra       |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+---------+----------+-------------+
|  1 | SIMPLE      | sbtest1 | NULL       | index | NULL          | PRIMARY | 4       | NULL | 4808163 |   100.00 | Using index |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+---------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
</code></pre>
<p>结果显示 <code>select count(*)</code> 走的是主键索引。</p>
<h4>验证二级索引</h4>
<p>创建一个二级索引：</p>
<pre><code>mysql&gt; create index k_1 on sbtest1(k);
Query OK, 0 rows affected (53.61 sec)
Records: 0  Duplicates: 0  Warnings: 0
</code></pre>
<p>为了验证本次过程，我们重启一下 MySQL，目的是清空 MySQL 的缓存。</p>
<pre><code>......  
MySQL 重启完成  
......  
</code></pre>
<p>查询 MySQL 缓存区，确保缓冲区中不存在测试表的缓存：</p>
<pre><code>mysql&gt; select * from sys.innodb_buffer_stats_by_table where object_schema = 'sbtest';
Empty set (0.05 sec)
</code></pre>
<p>执行 <code>select count(*)</code>：</p>
<pre><code>mysql&gt; select count(*) from sbtest1;
+----------+
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (0.73 sec)
</code></pre>
<p>再次查看 MySQL 缓存区，查询测试表的缓存：</p>
<pre><code>mysql&gt; select * from sys.innodb_buffer_stats_by_table where object_schema = 'sbtest';
+---------------+-------------+-----------+-----------+-------+--------------+-----------+-------------+
| object_schema | object_name | allocated | data      | pages | pages_hashed | pages_old | rows_cached |
+---------------+-------------+-----------+-----------+-------+--------------+-----------+-------------+
| sbtest        | sbtest1     | 65.09 MiB | 62.06 MiB |  4166 |            0 |      1459 |     2501935 |
+---------------+-------------+-----------+-----------+-------+--------------+-----------+-------------+
1 row in set (0.08 sec)
</code></pre>
<p>结果显示：缓存了 60M+ 的数据。</p>
<p>查看执行计划：</p>
<pre><code>mysql&gt; explain select count(*) from sbtest1;
+----+-------------+---------+------------+-------+---------------+------+---------+------+---------+----------+-------------+
| id | select_type | table   | partitions | type  | possible_keys | key  | key_len | ref  | rows    | filtered | Extra       |
+----+-------------+---------+------------+-------+---------------+------+---------+------+---------+----------+-------------+
|  1 | SIMPLE      | sbtest1 | NULL       | index | NULL          | k_1  | 4       | NULL | 4808163 |   100.00 | Using index |
+----+-------------+---------+------------+-------+---------------+------+---------+------+---------+----------+-------------+
1 row in set, 1 warning (0.01 sec)
</code></pre>
<p>结果显示 <code>select count(*)</code> 走的是二级索引 k_1。</p>
<h4>更加直观看一下两种索引占用的空间大小</h4>
<p>首先我们查看一下 MySQL 的 innodb_page_size 的大小：</p>
<pre><code>mysql&gt; show variables like 'Innodb_page_size';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| innodb_page_size | 16384 |
+------------------+-------+
1 row in set (0.01 sec)
</code></pre>
<p>大小是 16K。</p>
<p>统计一下聚簇索引和二级索引占用的空间大小：</p>
<pre><code>mysql&gt; select 
    -&gt;   sum(stat_value) pages,
    -&gt;   index_name index_name,
    -&gt;   (round((sum(stat_value) * @@innodb_page_size)/1024/1024)) as MB
    -&gt;   from mysql.innodb_index_stats 
    -&gt;   where table_name = 'sbtest1' AND database_name = 'sbtest' AND stat_description = 'Number of pages in the index' 
    -&gt; group by index_name;
+-------+------------+------+
| pages | index_name | MB   |
+-------+------------+------+
| 67456 | PRIMARY    | 1054 |
|  4774 | k_1        |   75 |
+-------+------------+------+
2 rows in set (0.01 sec)
</code></pre>
<p>这样结果太明显了，主键索引占用了几乎 1 个 G 的空间，而 k_1 这个二级索引值占用了 75M 的空间。</p>
<h3>总结与思考</h3>
<p>MySQL 的 <code>select count(*)</code> 在底层实现统计的过程中通过二级索引优于主键索引优于全表扫描，这是因为二级索引只缓存主键列和索引列，主键索引几乎缓存了所有的行记录，前者势必比后者缓存的内容少的多，当然计算的效率肯定要快的多。</p>
<p>我们再思考一下，假如数据量不是 500W，而二级索引占用的空间都 1G、10G，甚至几十 G 了，速度也就不可接受了，怎么办？</p>
<p>这个时候我们不能局限于二级索引了，而可考虑：</p>
<ol>
<li>单纯的统计，我们可以考虑用 MyISAM 引擎，它自带计数器，当然了，局限性就不一一列举了，此方案了解即可吧。</li>
<li>数据仓库等其他可接入的系统来完成此工作。</li>
<li>缓存中间件也不失一个好的建议。</li>
<li>做一个类似触发器计数的功能？</li>
<li>MySQL 8.0 的并行查询，嗯，好功能。</li>
<li>历史数据迁移，就不让你查询那么多数据了，这个有点霸道了，可以换着说法，根据业务需求，历史数据迁移，只保留某些数据（按规则）。</li>
<li>分库分表，不多说什么，还是物理上的优化。</li>
<li>服务器硬件资源提升，比如 SSD 硬盘等（治标不治本）。</li>
<li>其他（肯定不止以上 8 种，如果你还有其他想法，请尊留言）。</li>
</ol>
<p>好了，至此我们基本学习完 select count(*)相关内容了，内容比较多，当然也有不足之处，欢迎朋友们指正补充。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL事务_事务隔离级别详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL共享锁、排他锁、悲观锁、乐观锁.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43636b1b42645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
