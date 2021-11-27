<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL · 引擎特性 · 临时表那些事儿.md</title>
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

                    <a class="current-tab" href="MySQL&#32;·&#32;引擎特性&#32;·&#32;临时表那些事儿.md">MySQL · 引擎特性 · 临时表那些事儿.md</a>
                    

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
                        <div><h1>MySQL · 引擎特性 · 临时表那些事儿</h1>
<h2>前言</h2>
<p>相比于普通的用户数据表，MySQL/InnoDB中的临时表，大家应该会陌生很多。再加上不同的临时表创建的时机和创建的位置都不固定，这也进一步加大神秘感。最让人捉摸不透的是，临时表很多时候会先创建文件，然后什么都不做，就把文件删除，留一个句柄读写，给人的感觉是神龙见首不见尾。本文分析了详细MySQL各个版本临时表的处理方式，希望对大家有所帮助。</p>
<h2>综述</h2>
<p>准确的说，我们常说的临时表分为两种，一种真的是表，用来存储用户发送的数，读写走的是表读写接口，读写的时候表一定在文件系统上存在，另外一种，应该是一种临时文件，用来存储SQL计算中间过程的数据，读写走的是文件读写接口，读写的时候文件可能已经被删除了，留一个文件句柄进行操作。</p>
<h3>临时表</h3>
<p>临时表可以分为磁盘临时表和内存临时表，而临时文件，只会存在于磁盘上，不会存在于内存中。具体来说，临时表的内存形态有Memory引擎和Temptable引擎，主要区别是对字符类型(varchar, blob，text类型)的存储方式，前者不管实际字符多少，都是用定长的空间存储，后者会用变长的空间存储，这样提高了内存中的存储效率，有更多的数据可以放在内存中处理而不是转换成磁盘临时表。Memory引擎从早期的5.6就可以使用，Temptable是8.0引入的新的引擎。另外一方面，磁盘临时表也有三种形态，一种是MyISAM表，一种是InnoDB临时表，另外一种是Temptable的文件map表。其中最后一种方式，是8.0提供的。</p>
<p>在5.6以及以前的版本，磁盘临时表都是放在数据库配置的临时目录，磁盘临时表的undolog都是与普通表的undo放在一起(注意由于磁盘临时表在数据库重启后就被删除了，不需要redolog通过奔溃恢复来保证事务的完整性，所以不需要写redolog，但是undolog还是需要的，因为需要支持回滚)。</p>
<p>在MySQL 5.7后，磁盘临时表的数据和undo都被独立出来，放在一个单独的表空间ibtmp1里面。之所以把临时表独立出来，主要是为了减少创建删除表时维护元数据的开销。</p>
<p>在MySQL 8.0后，磁盘临时表的数据单独放在Session临时表空间池(#innodb_temp目录下的ibt文件)里面，临时表的undo放在global的表空间ibtmp1里面。另外一个大的改进是，8.0的磁盘临时表数据占用的空间在连接断开后，就能释放给操作系统，而5.7的版本中需要重启才能释放。</p>
<p>目前有以下两种情况会用到临时表：</p>
<h4>用户显式创建临时表</h4>
<p>这种是用户通过显式的执行命令<code>create temporary table</code>创建的表，引擎的类型要么显式指定，要么使用默认配置的值(default_tmp_storage_engine)。内存使用就遵循指定引擎的内存管理方式，比如InnoDB的表会先缓存在Buffer Pool中，然后通过刷脏线程写回磁盘文件。</p>
<p>在5.6中，磁盘临时表位于tmpdir下，文件名类似<code>#sql4d2b_8_0.ibd</code>，其中<code>#sql</code>是固定的前缀，<code>4d2b</code>是进程号的十六进制表示，<code>8</code>是MySQL线程号的十六进制表示(show processlist中的id)，<code>0</code>是每个连接从0开始的递增值，<code>ibd</code>是innodb的磁盘临时表(通过参数<code>default_tmp_storage_engine</code>控制)。在5.6中，磁盘临时表创建好后，对应的frm以及引擎文件就在tmpdir下创建完毕，可以通过文件系统ls命令查看到。在连接关闭后，相应文件自动删除。因此，我们如果在5.6的tmpdir里面看到很多类似格式文件名，可以通过文件名来判断是哪个进程，哪个连接使用的临时表，这个技巧在排查tmpdir目录占用过多空间的问题时，尤其适用。用户显式创建的这种临时表，在连接释放的时候，会自动释放并把空间释放回操作系统。临时表的undolog存在undo表空间中，与普通表的undo放在一起。有了undo回滚段，用户创建的这种临时表也能支持回滚了。</p>
<p>在5.7中，临时磁盘表位于ibtmp文件中，ibtmp文件位置及大小控制方式由参数<code>innodb_temp_data_file_path</code>控制。显式创建的表的数据和undo都在ibtmp里面。用户连接断开后，临时表会释放，但是仅仅是在ibtmp文件里面标记一下，空间是不会释放回操作系统的。如果要释放空间，需要重启数据库。另外，需要注意的一点是，5.6可以在tmpdir下直接看到创建的文件，但是5.7是创建在ibtmp这个表空间里面，因此是看不到具体的表文件的。如果需要查看，则需要查看<code>INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO</code>这个表，里面有一列name，这里可以看到表名。命名规格与5.6的类似，因此也可以快速找到占用空间大的连接。</p>
<p>在8.0中，临时表的数据和undo被进一步分开，数据是存放在ibt文件中(由参数<code>innodb_temp_tablespaces_dir</code>控制)，undo依然存放在ibtmp文件中(依然由参数<code>innodb_temp_data_file_path</code>控制)。存放ibt文件的叫做Session临时表空间，存放undo的ibtmp叫做Global临时表空间。这里介绍一下这个存放数据的Session临时表空间。Session临时表空间，在磁盘上的表现是一组以ibt文件组成的文件池。启动的时候，数据库会在配置的目录下重新创建，关闭数据库的时候删除。启动的时候，默认会创建10个ibt文件，每个连接最多使用两个，一个给用户创建的临时表用，另外一个给下文描述的优化器创建的隐式临时表使用。当然只有在需要临时表的时候，才会创建，如果不需要，则不会占用ibt文件。当10个ibt都被使用完后，数据库会继续创建，最多创建四十万个。当连接释放时候，会自动把这个连接使用的ibt文件给释放，同时回收空间。如果要回收Global临时表空间，依然需要重启。但是由于已经把存放数据的文件分离出来，且其支持动态回收(即连接断开即释放空间)，所以5.7上困扰大家多时的空间占用问题，已经得到了很好的缓解。当然，还是有优化空间的，例如，空间需要在连接断开后，才能释放，而理论上，很多空间在某些SQL(如用户drop了某个显式创建的临时表)执行后，即可以释放。另外，如果需要查看表名，依然查看<code>INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO</code>这个表。需要注意的是，8.0上，显式临时表不能是压缩表，而5.6和5.7可以。</p>
<h4>优化器隐式创建临时表</h4>
<p>这种临时表，是数据库为了辅助某些复杂SQL的执行而创建的辅助表，是否需要临时表，一般都是由优化器决定。与用户显式创建的临时表直接创建磁盘文件不同，如果需要优化器觉得SQL需要临时表辅助，会先使用内存临时表，如果超过配置的内存(min(tmp_table_size, max_heap_table_siz))，就会转化成磁盘临时表，这种磁盘临时表就类似用户显式创建的，引擎类型通过参数<code>internal_tmp_disk_storage_engine</code>控制。一般稍微复杂一点的查询，包括且不限于order by, group by, distinct等，都会用到这种隐式创建的临时表。用户可以通过explain命令，在Extra列中，看是否有Using temporary这样的字样，如果有，就肯定要用临时表。</p>
<p>在5.6中，隐式临时表依然在tmpdir下，在复杂SQL执行的过程中，就能看到这临时表，一旦执行结束，就被删除。值得注意的是，5.6中，这种隐式创建的临时表，只能用MyISAM引擎，即没有<code>internal_tmp_disk_storage_engine</code>这个参数可以控制。所以，当我们的系统中只有innodb表时，也会看到MyISAM的某些指标在变动，这种情况下，一般都是隐式临时表的原因。</p>
<p>在5.7中，隐式临时表是创建在ibtmp文件中的，SQL结束后，会标记删除，但是空间依然不会返还给操作系统，如果需要返还，则需要重启数据库。另外，5.7支持参数<code>internal_tmp_disk_storage_engine</code>，用户可以选择InnoDB或者MYISAM表作为磁盘临时表。</p>
<p>在8.0中，隐式临时表是创建在Session临时表空间中的，即与用户显式创建的临时表的数据放在一起。如果一个连接第一次需要隐式临时表，那么数据库会从ibt文件构成的池子中取出一个给这个连接使用，直到连接释放。上文中，我们也提到过，在8.0中，用户显式创建的临时表也会从池子中分配一个ibt来使用，每个连接最多使用两个ibt文件用来存储临时表。我们可以查询<code>INFORMATION_SCHEMA.INNODB_SESSION_TEMP_TABLESPACES</code>来确定ibt文件的去向。这个表中，每个ibt文件是一行，当前系统中有几个ibt文件就有几行。有一列叫做ID，如果此列为0，表示此ibt没有被使用，如果非0，表示被此ID的连接在用，比如ID为8，则表示process_id为8的连接在用这个ibt文件。另外，还有一列purpose，值为INTRINSIC表示是隐式临时表在用这个ibt，USER则表示是显示临时表在用。此外，还有一列size，表示当前的大小。用户可以查询这个表来确定整个数据库临时表的使用情况，十分方便。</p>
<p>在5.6和5.7中，内存临时表只能使用Memory引擎，到了8.0，多了一种Temptable引擎的选择。Temptable在存储格式有采用了变长存储，可以节省存储空间，进一步提高内存使用率，减少转换成磁盘临时表的次数。如果设置的磁盘临时表是InnoDB或者MYISAM，则需要一个转换拷贝的消耗。为了尽可能减少消耗，Temptable提出了一种overflow机制，即如果内存临时表超过配置大小，则使用磁盘空间map的方式，即打开一个文件，然后删除，留一个句柄进行读写操作。读写文件格式和内存中格式一样，这样就略过了转换这一步，进一步提高性能。注意，这个功能是在还没发布的8.0.16版本中才有的，因为还看不到代码，只能通过文档猜测其实现。在8.0.16中，参数<code>internal_tmp_disk_storage_engine</code>已经被去掉，磁盘临时表只能使用InnoDB形式或者TempTable的这种overflow形式。从文档中，我们似乎看出官方比较推荐使用TempTable这个新的引擎。具体性能提升情况，还需要等代码发布后，测试过才能得出结论。</p>
<h3>临时文件</h3>
<p>相比临时表，临时文件对大家可能更加陌生，临时文件更多的被使用在缓存数据，排序数据的场景中。一般情况下，被缓存或者排序的数据，首先放在内存中，如果内存放不下，才会使用磁盘临时文件的方式。临时文件的使用方式与一般的表也不太一样，一般的表创建完后，就开始读写数据，使用完后，才把文件删除，但是临时文件的使用方式不一样，在创建完后(使用mkstemp系统函数)，马上调用unlink删除文件，但是不close文件，后续使用原来的句柄操作文件。这样的好处是，当进程异常crash，不会有临时文件因为没被删除而残留，但是坏处也是明显的，我们在文件系统上使用ls命令就看不到这个文件，需要使用lsof +L1来查看这种deleted属性的文件。</p>
<p>目前，我们主要在一下场景使用临时文件：</p>
<h4>DDL中的临时文件</h4>
<p>在做online DDL的过程中，很多操作需要对原表进行重建，对表重建前，需要对各种二级索引排序，而大量数据的排序，不太可能在内存中完成，需要依赖外部排序算法，MySQL使用了归并排序。这个过程中就需要创建临时文件。一般需要的空间大小与原表差不多。但是在使用完之后，会马上清理，所以在做DDL的时候，需要保留出足够的空间。用户可以通过指定innodb_tmpdir来指定这种排序文件的路径。这个参数可以动态修改，一般把他设置在有足够磁盘空间的路径上。临时文件的名字一般是类似<code>ibXXXXXX</code>，其中<code>ib</code>是固定前缀，<code>XXXXXX</code>是大小写字母以及数字的随机组合。</p>
<p>在做online DDL中，我们是允许用户对原表做DML操作的，即增删改查。我们不能直接插入原表中，因此需要一个地方记录对原表的修改操作，在DDL结束后，再应用在新表上。这个记录的地方就是online log，当然如果改动少的话，直接存在内存里(参数<code>innodb_sort_buffer_size</code>可控制，同时这个参数也控制online log每个读写块的大小)面即可。这个onlinelog也是用临时文件存，创建在innodb_tmpdir，最大大小为参数<code>innodb_online_alter_log_max_size</code>控制，如果超过这个大小了，DDL就会失败。临时文件的名字也类似上述的排序临时文件的名字。</p>
<p>在online DDL的最后阶段，需要把排序完的文件和中途产生的DML全都应用到一个中间文件上，中间文件文件名类似<code>#sql-ib53-522550444.ibd</code>，其中<code>#sql-ib</code>是固定的前缀，<code>53</code>是InnoDB层的table id，<code>522550444</code>是随机生成的数字。同时，在server层也会生成一个frm文件(8.0中没有)，文件名类似<code>#sql-4d2b_2a.frm</code>，其中<code>#sql</code>是固定前缀，<code>4d2b</code>是进程号的十六进制表示，<code>2a</code>是线程号的十六进制表示(show processlist中的id)。因此我们也可以通过这个命名规则来找到哪个线程在做DDL。这里需要注意一点，这里说的中间文件，其实算是一个临时表，并不是上文说中临时文件，这些中间文件可以通过ls来查看。当在DDL中的最后一步，会把这两个临时文件命名回原来的表名。正因为这个特性，所以当数据库中途crash的时候，可能会在磁盘上留下残余无用的文件。遇到这种情况，可以先把frm文件重命名成与ibd文件一样的名字，然后使用<code>DROP TABLE</code>#mysql50##sql-ib53-522550444`来清理残余的文件。注意，如果不用drop命令，直接删除ibd文件，可能会导致数据字典里面依然有残余的信息，做法不太优雅。当然，在8.0中，由于使用了原子的数据字典，就不会出现这种残余文件了。</p>
<h4>BinLog中的缓存操作</h4>
<p>BinLog只有在事务提交的时候才会写入到文件中，在没提交前，会先放在内存中(由参数<code>binlog_cache_size</code>控制)，如果内存放慢了，就会创建临时文件，使用方法也是先通过mkstemp创建，然后直接unlink，留一个句柄读写。临时文件名类似<code>MLXXXXXX</code>，其中<code>ML</code>是固定前缀，<code>XXXXXX</code>是大小写字母以及数字的随机组合。单个事务的BinLog太大，可能会导致整个BinLog的大小也过大，从而影响同步，因此我们需要尽可能控制事务大小。</p>
<h4>优化创建的临时文件</h4>
<p>有些操作，除了在引擎层需要依赖隐式临时表来辅助复杂SQL的计算，在Server层，也会创建临时文件来辅助，比如order by操作，会调用filesort函数。这个函数也会先使用内存(sort_buffer_size)排序，如果不够，就会创建一个临时文件，辅助排序。文件名类似<code>MYXXXXXX</code>，其中<code>MY</code>是固定前缀，<code>XXXXXX</code>是大小写字母以及数字的随机组合。</p>
<h4>Load data中用的临时文件</h4>
<p>在BinLog复制中，如果在主库上使用了Load Data命令，即从文件中导数据，数据库会把整个文件写入到RelayLog中，然后传到备库，备库解析RelayLog，从中抽取出对应的Load文件，然后在备库上应用。备库上这个文件存储的位置由参数<code>slave_load_tmpdir</code>控制。文档中建议这个目录不要配置在物理机的内存目录或者重启后会删除的目录。因为复制依赖这个文件，如果意外被删除，会导致复制中断。</p>
<h4>其他</h4>
<p>除了上文所述的几个地方外，还有其他几个地方也会用到临时文件：</p>
<ul>
<li>在InnoDB层，启动的时候会创建多个临时文件用来存储：最后一次外键或者唯一键错误; 最后一次死锁的信息; 最后的innodb状态信息。用临时文件而不用内存的原因猜测是，内存使用率不会因为写这些指标而波动。</li>
<li>在Server层，分区表使用show create table时，会用到临时文件。另外在MYISAM表内部排序的时候也会用到临时文件。</li>
</ul>
<h2>相关参数</h2>
<p>** tmpdir: ** 这个参数是临时目录的配置，在5.6以及之前的版本，临时表/文件默认都会放在这里。这个参数可以配置多个目录，这样就可以轮流在不同的目录上创建临时表/文件，如果不同的目录分别指向不同的磁盘，就可以达到分流的目的。
** innodb_tmpdir: ** 这个参数只要是被DDL中的排序临时文件使用的。其占用的空间会很大，建议单独配置。这个参数可以动态设置，也是一个Session变量。
** slave_load_tmpdir: ** 这个参数主要是给BinLog复制中Load Data时，配置备库存放临时文件位置时使用。因为数据库Crash后还需要依赖Load数据的文件，建议不要配置重启后会删除数据的目录。
** internal_tmp_disk_storage_engine: ** 当隐式临时表被转换成磁盘临时表时，使用哪种引擎，默认只有MyISAM和InnoDB。5.7及以后的版本才支持。8.0.16版本后取消的这个参数。
** internal_tmp_mem_storage_engine: ** 隐式临时表在内存时用的存储引擎，可以选择Memory或者Temptable引擎。建议选择新的Temptable引擎。
** default_tmp_storage_engine: ** 默认的显式临时表的引擎，即用户通过SQL语句创建的临时表的引擎。
** tmp_table_size: ** min(tmp_table_size,max_heap_table_size)是隐式临时表的内存大小，超过这个值会转换成磁盘临时表。
** max_heap_table_size: ** 用户创建的Memory内存表的内存限制大小。
** big_tables: ** 内存临时表转换成磁盘临时表需要有个转化操作，需要在不同引擎格式中转换，这个是需要消耗的。如果我们能提前知道执行某个SQL需要用到磁盘临时表，即内存肯定不够用，可以设置这个参数，这样优化器就跳过使用内存临时表，直接使用磁盘临时表，减少开销。
** temptable_max_ram: ** 这个参数是8.0后才有的，主要是给Temptable引擎指定内存大小，超过这个后，要么就转换成磁盘临时表，要么就使用自带的overflow机制。
** temptable_use_mmap: ** 是否使用Temptable的overflow机制。</p>
<h2>总结建议</h2>
<p>MySQL的临时表以及临时文件其实是一个比较复杂的话题，涉及的模块比较多，出现的时机比较难把握，导致排查问题相比普通表也难不少。建议读者结合代码细细研究，这样才能定位在线上可能出现的棘手问题。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB崩溃恢复.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;主从复制&#32;半同步复制.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4362e92a02645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
