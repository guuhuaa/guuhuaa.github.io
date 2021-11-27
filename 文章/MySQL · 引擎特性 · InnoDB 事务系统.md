<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>MySQL · 引擎特性 · InnoDB 事务系统.md</title>
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

                    <a class="current-tab" href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;事务系统.md">MySQL · 引擎特性 · InnoDB 事务系统.md</a>
                    

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
                        <div><h1>MySQL · 引擎特性 · InnoDB 事务系统</h1>
<h2>前言</h2>
<p>关系型数据库的事务机制因其有原子性，一致性等优秀特性深受开发者喜爱，类似的思想已经被应用到很多其他系统上，例如文件系统等。本文主要介绍InnoDB事务子系统，主要包括，事务的启动，事务的提交，事务的回滚，多版本控制，垃圾清理，回滚段以及相应的参数和监控方法。代码主要基于RDS 5.6，部分特性已经开源到AliSQL。事务系统是InnoDB最核心的中控系统，涉及的代码比较多，主要集中在trx目录，read目录以及row目录中的一部分，包括头文件和IC文件，一共有两万两千多行代码。</p>
<h2>基础知识</h2>
<p>**事务ACID: ** 原子性，指的是整个事务要么全部成功，要么全部失败，对InnoDB来说，只要client收到server发送过来的commit成功报文，那么这个事务一定是成功的。如果收到的是rollback的成功报文，那么整个事务的所有操作一定都要被回滚掉，就好像什么都没执行过一样。另外，如果连接中途断开或者server crash事务也要保证会滚掉。InnoDB通过undolog保证rollback的时候能找到之前的数据。一致性，指的是在任何时刻，包括数据库正常提供服务的时候，数据库从异常中恢复过来的时候，数据都是一致的，保证不会读到中间状态的数据。在InnoDB中，主要通过crash recovery和double write buffer的机制保证数据的一致性。隔离性，指的是多个事务可以同时对数据进行修改，但是相互不影响。InnoDB中，依据不同的业务场景，有四种隔离级别可以选择。默认是RR隔离级别，因为相比于RC，InnoDB的RR性能更加好。持久性，值的是事务commit的数据在任何情况下都不能丢。在内部实现中，InnoDB通过redolog保证已经commit的数据一定不会丢失。</p>
<p>**多版本控制: ** 指的是一种提高并发的技术。最早的数据库系统，只有读读之间可以并发，读写，写读，写写都要阻塞。引入多版本之后，只有写写之间相互阻塞，其他三种操作都可以并行，这样大幅度提高了InnoDB的并发度。在内部实现中，与Postgres在数据行上实现多版本不同，InnoDB是在undolog中实现的，通过undolog可以找回数据的历史版本。找回的数据历史版本可以提供给用户读(按照隔离级别的定义，有些读请求只能看到比较老的数据版本)，也可以在回滚的时候覆盖数据页上的数据。在InnoDB内部中，会记录一个全局的活跃读写事务数组，其主要用来判断事务的可见性。</p>
<p>**垃圾清理: ** 对于用户删除的数据，InnoDB并不是立刻删除，而是标记一下，后台线程批量的真正删除。类似的还有InnoDB的二级索引的更新操作，不是直接对索引进行更新，而是标记一下，然后产生一条新的。这个线程就是后台的Purge线程。此外，过期的undolog也需要回收，这里说的过期，指的是undo不需要被用来构建之前的版本，也不需要用来回滚事务。</p>
<p>**回滚段: ** 可以理解为数据页的修改链，链表最前面的是最老的一次修改，最后面的最新的一次修改，从链表尾部逆向操作可以恢复到数据最老的版本。在InnoDB中，与之相关的还有undo tablespace, undo segment, undo slot, undo log这几个概念。undo log是最小的粒度，所在的数据页称为undo page，然后若干个undo page构成一个undo slot。一个事务最多可以有两个undo slot，一个是insert undo slot, 用来存储这个事务的insert undo，里面主要记录了主键的信息，方便在回滚的时候快速找到这一行。另外一个是update undo slot，用来存储这个事务delete/update产生的undo，里面详细记录了被修改之前每一列的信息，便于在读请求需要的时候构造。1024个undo slot构成了一个undo segment。然后若干个undo segemnt构成了undo tablespace。</p>
<p>**历史链表: ** insert undo可以在事务提交/回滚后直接删除，没有事务会要求查询新插入数据的历史版本，但是update undo则不可以，因为其他读请求可能需要使用update undo构建之前的历史版本。因此，在事务提交的时候，会把update undo加入到一个全局链表(<code>history list</code>)中，链表按照事务提交的顺序排序，保证最先提交的事务的update undo在前面，这样Purge线程就可以从最老的事务开始做清理。这个链表如果太长说明有很多记录没被彻底删除，也有很多undolog没有被清理，这个时候就需要去看一下是否有个长事务没提交导致Purge线程无法工作。在InnoDB具体实现上，history list其实只是undo segment维度的，全局的history list采用最小堆来实现，最小堆的元素是某个undo segment中最小事务no对应的undopage。当这个undolog被Purge清理后，通过history list找到次小的，然后替换掉最小堆元素中的值，来保证下次Purge的顺序的正确性。</p>
<p>**回滚点: ** 又称为savepoint，事务回滚的时候可以指定回滚点，这样可以保证回滚到指定的点，而不是回滚掉整个事务，对开发者来说，这是一个强大的功能。在InnoDB内部实现中，每打一个回滚点，其实就是保存一下当前的undo_no，回滚的时候直接回滚到这个undo_no点就可以了。</p>
<h2>核心数据结构</h2>
<p>在分析核心的代码之前，先介绍一下几个核心的数据结构。这些结构贯穿整个事务系统，理解他们对理解整个InnoDB的工作原理也颇有帮助。</p>
<p>**trx_t: ** 整个结构体每个连接持有一个，也就是在创建连接后执行第一个事务开始，整个结构体就被初始化了，后续这个连接的所有事务一直复用里面的数据结构，直到这个连接断开。同时，事务启动后，就会把这个结构体加入到全局事务链表中(<code>trx_sys-&gt;mysql_trx_list</code>)，如果是读写事务，还会加入到全局读写事务链表中(<code>trx_sys-&gt;rw_trx_list</code>)。在事务提交的时候，还会加入到全局提交事务链表中(<code>trx_sys-&gt;trx_serial_list</code>)。state字段记录了事务四种状态:<code>TRX_STATE_NOT_STARTED</code>, <code>TRX_STATE_ACTIVE</code>, <code>TRX_STATE_PREPARED</code>, <code>TRX_STATE_COMMITTED_IN_MEMORY</code>。
这里有两个字段值得区分一下，分别是id和no字段。id是在事务刚创建的时候分配的(只读事务永远为0，读写事务通过一个全局id产生器产生，非0)，目的就是为了区分不同的事务(只读事务通过指针地址来区分)，而no字段是在事务提交前，通过同一个全局id生产器产生的，主要目的是为了确定事务提交的顺序，保证加入到<code>history list</code>中的update undo有序，方便purge线程清理。
此外，trx_t结构体中还有自己的read_view用来表示当前事务的可见范围。分配的insert undo slot和update undo slot。如果是只读事务，read_only也会被标记为true。</p>
<p>**trx_sys_t: ** 这个结构体用来维护系统的事务信息，全局只有一个，在数据库启动的时候初始化。比较重要的字段有：max_trx_id，这个字段表示系统当前还未分配的最小事务id，如果有一个新的事务，直接把这个值作为新事务的id，然后这个字段递增即可。descriptors，这个是一个数组，里面存放着当前所有活跃的读写事务id，当需要开启一个readview的时候，就从这个字段里面拷贝一份，用来判断记录的对事务的可见性。rw_trx_list，这个主要是用来存放当前系统的所有读写事务，包括活跃的和已经提交的事务。按照事务id排序，此外，奔溃恢复后产生的事务和系统的事务也放在上面。mysql_trx_list，这里面存放所有用户创建的事务，系统的事务和奔溃恢复后的事务不会在这个链表上，但是这个链表上可能会有还没开始的用户事务。trx_serial_list，按照事务no(trx_t-&gt;no)排序的已经提交的事务。rseg_array，这个指向系统所有可以用的回滚段(<code>undo segments</code>)，当某个事务需要回滚段的时候，就从这里分配。rseg_history_len， 所有提交事务的update undo的长度，也就是上文提到的历史链表的长度，具体的update undo链表是存放在这个undo log中以文件指针的形式管理起来。view_list，这个是系统当前所有的readview, 所有开启的readview的事务都会把自己的readview放在这个上面，按照事务no排序。</p>
<p>**trx_purge_t: ** Purge线程使用的结构体，全局只有一个，在系统启动的时候初始化。view，是一个readview，Purge线程不会尝试删除所有大于view-&gt;low_limit_no的undolog。limit，所有小于这个值的undolog都可以被truncate掉，因为标记的日志已经被删除且不需要用他们构建之前的历史版本。此外，还有rseg，page_no, offset，hdr_page_no, hdr_offset这些字段，主要用来保存最后一个还未被purge的undolog。</p>
<p>**read_view_t: ** InnDB为了判断某条记录是否对当前事务可见，需要对此记录进行可见性判断，这个结构体就是用来辅助判断的。每个连接都的trx_t里面都有一个readview，在事务需要一致性的读时候(不同隔离级别不同)，会被初始化，在读结束的时候会释放(缓存)。low_limit_no，这个主要是给purge线程用，readview创建的时候，会把当前最小的提交事务id赋值给low_limit_no，这样Purge线程就可以把所有已经提交的事务的undo日志给删除。low_limit_id, 所有大于等于此值的记录都不应该被此readview看到，可以理解为high water mark。up_limit_id, 所有小于此值的记录都应该被此readview看到，可以理解为low water mark。descriptors, 这是一个数组，里面存了readview创建时候所有全局读写事务的id，除了事务自己做的变更外，此readview应该看不到descriptors中事务所做的变更。view_list，每个readview都会被加入到trx_sys中的全局readview链表中。</p>
<p>**trx_id_t: ** 每个读写事务都会通过全局id产生器产生一个id，只读事务的事务id为0，只有当其切换为读写事务时候再分配事务id。为了保证在任何情况下(包括数据库不断异常恢复)，事务id都不重复，InnoDB的全局id产生器每分配256(<code>TRX_SYS_TRX_ID_WRITE_MARGIN</code>)个事务id，就会把当前的max_trx_id持久化到ibdata的系统页上面。此外，每次数据库重启，都从系统页上读取，然后加上256(<code>TRX_SYS_TRX_ID_WRITE_MARGIN</code>)。</p>
<p>**trx_rseg_t: ** undo segment内存中的结构体。每个undo segment都对应一个。update_undo_list表示已经被分配出去的正在使用的update undo链表，insert_undo_list表示已经被分配出去的正在使用的insert undo链表。update_undo_cached和insert_undo_cached表示缓存起来的undo链表，主要为了快速使用。last_page_no, last_offset, last_trx_no, last_del_marks表示这个undo segment中最后没有被Purge的undolog。</p>
<h2>事务的启动</h2>
<p>在InnoDB里面有两种事务，一种是读写事务，就是会对数据进行修改的事务，另外一种是只读事务，仅仅对数据进行读取。读写事务需要比只读事务多做以下几点工作：首先，需要分配回滚段，因为会修改数据，就需要找地方把老版本的数据给记录下来，其次，需要通过全局事务id产生器产生一个事务id，最后，把读写事务加入到全局读写事务链表(<code>trx_sys-&gt;rw_trx_list</code>)，把事务id加入到活跃读写事务数组中(<code>trx_sys-&gt;descriptors</code>)。因此，可以看出，读写事务确实需要比只读事务多做不少工作，在使用数据库的时候尽可能把事务申明为只读。</p>
<p><code>start transaction</code>语句启动事务。这种语句和<code>begin work</code>,<code>begin</code>等效。这些语句默认是以只读事务的方式启动。<code>start transaction read only</code>语句启动事务。这种语句就把<code>thd-&gt;tx_read_only</code>置为true，后续如果做了DML/DDL等修改数据的语句，会返回错误<code>ER_CANT_EXECUTE_IN_READ_ONLY_TRANSACTION</code>。<code>start transaction read write</code>语句启动事务。这种语句会把<code>thd-&gt;tx_read_only</code>置为true，此外，允许super用户在read_only参数为true的情况下启动读写事务。<code>start transaction with consistent snapshot</code>语句启动事务。这种启动方式还会进入InnoDB层，并开启一个readview。注意，只有在RR隔离级别下，这种操作才有效，否则会报错。</p>
<p>上述的几种启动方式，都会先去检查前一个事务是否已经提交，如果没有则先提交，然后释放MDL锁。此外，除了<code>with consistent snapshot</code>的方式会进入InnoDB层，其他所有的方式都只是在Server层做个标记，没有进入InnoDB做标记，在InnoDB看来所有的事务在启动时候都是只读状态，只有接受到修改数据的SQL后(InnoDB接收到才行。因为在<code>start transaction read only</code>模式下，DML/DDL都被Serve层挡掉了)才调用<code>trx_set_rw_mode</code>函数把只读事务提升为读写事务。</p>
<p>新建一个连接后，在开始第一个事务前，在InnoDB层会调用函数<code>innobase_trx_allocate</code>分配和初始化trx_t对象。默认的隔离级别为REPEATABLE_READ，并且加入到<code>mysql_trx_list</code>中。注意这一步仅仅是初始化trx_t对象，但是真正开始事务的是函数<code>trx_start_low</code>，在<code>trx_start_low</code>中，如果当前的语句只是一条只读语句，则先以只读事务的形式开启事务，否则按照读写事务的形式，这就需要分配事务id，分配回滚段等。</p>
<h2>事务的提交</h2>
<p>相比于事务的启动，事务的提交就复杂许多。这里只介绍事务在InnoDB层的提交过程，Server层涉及到与Binlog的XA事务暂时不介绍。入口函数为<code>innobase_commit</code>。</p>
<p>函数有一个参数<code>commit_trx</code>来控制是否真的提交，因为每条语句执行结束的时候都会调用这个函数，而不是每条语句执行结束的时候事务都提交。如果这个参数为true，或者配置了<code>autocommit=1</code>, 则进入提交的核心逻辑。否则释放因为auto_inc而造成的表锁，并且记录undo_no(回滚单条语句的时候用到，相关参数<code>innodb_rollback_on_timeout</code>)。
提交的核心逻辑：</p>
<ol>
<li>依据参数innobase_commit_concurrency来判断是否有过多的线程同时提交，如果太多则等待。</li>
<li>设置事务状态为committing，我们可以在<code>show processlist</code>看到(<code>trx_commit_for_mysql</code>)。</li>
<li>使用全局事务id产生器生成事务no，然后把事务trx_t加入到<code>trx_serial_list</code>。如果当前的undo segment没有设置最后一个未Purge的undo，则用此事务no更新(<code>trx_serialisation_number_get</code>)。</li>
<li>标记undo，如果这个事务只使用了一个undopage且使用量小于四分之三个page，则把这个page标记为(<code>TRX_UNDO_CACHED</code>)。如果不满足且是insert undo则标记为<code>TRX_UNDO_TO_FREE</code>，否则undo为update undo则标记为<code>TRX_UNDO_TO_PURGE</code>。标记为<code>TRX_UNDO_CACHED</code>的undo会被回收，方便下次重新利用(<code>trx_undo_set_state_at_finish</code>)。</li>
<li>把update undo放入所在undo segment的history list，并递增<code>trx_sys-&gt;rseg_history_len</code>(这个值是全局的)。同时更新page上的<code>TRX_UNDO_TRX_NO</code>, 如果删除了数据，则重置delete_mark(<code>trx_purge_add_update_undo_to_history</code>)。</li>
<li>把undate undo从update_undo_list中删除，如果被标记为<code>TRX_UNDO_CACHED</code>，则加入到update_undo_cached队列中(<code>trx_undo_update_cleanup</code>)。</li>
<li>在系统页中更新binlog名字和偏移量(<code>trx_write_serialisation_history</code>)。</li>
<li>mtr_commit，至此，在文件层次事务提交。这个时候即使crash，重启后依然能保证事务是被提交的。接下来要做的是内存数据状态的更新(<code>trx_commit_in_memory</code>)。</li>
<li>如果是只读事务，则只需要把readview从全局readview链表中移除，然后重置trx_t结构体里面的信息即可。如果是读写事务，情况则复杂点，首先需要是设置事务状态为<code>TRX_STATE_COMMITTED_IN_MEMORY</code>，其次，释放所有行锁，接着，trx_t从rw_trx_list中移除，readview从全局readview链表中移除，另外如果有insert undo则在这里移除(update undo在事务提交前就被移除，主要是为了保证添加到history list的顺序)，如果有update undo，则唤醒Purge线程进行垃圾清理，最后重置trx_t里的信息，便于下一个事务使用。</li>
</ol>
<h2>事务的回滚</h2>
<p>InnoDB的事务回滚是通过undolog来逆向操作来实现的，但是undolog是存在undopage中，undopage跟普通的数据页一样，遵循bufferpool的淘汰机制，如果一个事务中的很多undopage已经被淘汰出内存了，那么在回滚的时候需要重新把这些undopage从磁盘中捞上来，这会造成大量io，需要注意。此外，由于引入了savepoint的概念，事务不仅可以全部回滚，也可以回滚到某个指定点。</p>
<p>回滚的上层函数是<code>innobase_rollback_trx</code>，主要流程如下：</p>
<ol>
<li>如果是只读事务，则直接返回。</li>
<li>判断当前是回滚整个事务还是部分事务，如果是部分事务，则记录下需要保留多少个undolog，多余的都回滚掉，如果是全部回滚，则记录0(trx_rollback_step)。</li>
<li>从update undo和insert undo中找出最后一条undo，从这条undo开始回滚(<code>trx_roll_pop_top_rec_of_trx</code>)。</li>
<li>如果是update undo则调用<code>row_undo_mod</code>进行回滚，标记删除的记录清理标记，更新过的数据回滚到最老的版本。如果是insert undo则调用<code>row_undo_ins</code>进行回滚，插入操作，直接删除聚集索引和二级索引。</li>
<li>如果是在奔溃恢复阶段且需要回滚的undolog个数大于1000条，则输出进度。</li>
<li>如果所有undo都已经被回滚或者回滚到了指定的undo，则停止，并且调用函数<code>trx_roll_try_truncate</code>把undolog删除(由于不需要使用unod构建历史版本，所以不需要留给Purge线程)。
此外，需要注意的是，回滚的代码由于是嵌入在query graphy的框架中，因此有些入口函数不太好找。例如，确定回滚范围的是在函数<code>trx_rollback_step</code>中，真正回滚的操作是在函数<code>row_undo_step</code>中，两者都是在函数<code>que_thr_step</code>被调用。</li>
</ol>
<h2>多版本控制MVCC</h2>
<p>数据库需要做好版本控制，防止不该被事务看到的数据(例如还没提交的事务修改的数据)被看到。在InnoDB中，主要是通过使用readview的技术来实现判断。查询出来的每一行记录，都会用readview来判断一下当前这行是否可以被当前事务看到，如果可以，则输出，否则就利用undolog来构建历史版本，再进行判断，知道记录构建到最老的版本或者可见性条件满足。</p>
<p>在trx_sys中，一直维护这一个全局的活跃的读写事务id(<code>trx_sys-&gt;descriptors</code>)，id按照从小到大排序，表示在某个时间点，数据库中所有的活跃(已经开始但还没提交)的读写(必须是读写事务，只读事务不包含在内)事务。当需要一个一致性读的时候(即创建新的readview时)，会把全局读写事务id拷贝一份到readview本地(read_view_t-&gt;descriptors)，当做当前事务的快照。read_view_t-&gt;up_limit_id是read_view_t-&gt;descriptors这数组中最小的值，read_view_t-&gt;low_limit_id是创建readview时的max_trx_id，即一定大于read_view_t-&gt;descriptors中的最大值。当查询出一条记录后(记录上有一个trx_id，表示这条记录最后被修改时的事务id)，可见性判断的逻辑如下(<code>lock_clust_rec_cons_read_sees</code>)：</p>
<p>如果记录上的trx_id小于read_view_t-&gt;up_limit_id，则说明这条记录的最后修改在readview创建之前，因此这条记录可以被看见。</p>
<p>如果记录上的trx_id大于等于read_view_t-&gt;low_limit_id，则说明这条记录的最后修改在readview创建之后，因此这条记录肯定不可以被看家。</p>
<p>如果记录上的trx_id在up_limit_id和low_limit_id之间，且trx_id在read_view_t-&gt;descriptors之中，则表示这条记录的最后修改是在readview创建之时，被另外一个活跃事务所修改，所以这条记录也不可以被看见。如果trx_id不在read_view_t-&gt;descriptors之中，则表示这条记录的最后修改在readview创建之前，所以可以看到。</p>
<p>基于上述判断，如果记录不可见，则尝试使用undo去构建老的版本(<code>row_vers_build_for_consistent_read</code>)，直到找到可以被看见的记录或者解析完所有的undo。
针对RR隔离级别，在第一次创建readview后，这个readview就会一直持续到事务结束，也就是说在事务执行过程中，数据的可见性不会变，所以在事务内部不会出现不一致的情况。针对RC隔离级别，事务中的每个查询语句都单独构建一个readview，所以如果两个查询之间有事务提交了，两个查询读出来的结果就不一样。从这里可以看出，在InnoDB中，RR隔离级别的效率是比RC隔离级别的高。此外，针对RU隔离级别，由于不会去检查可见性，所以在一条SQL中也会读到不一致的数据。针对串行化隔离级别，InnoDB是通过锁机制来实现的，而不是通过多版本控制的机制，所以性能很差。</p>
<p>由于readview的创建涉及到拷贝全局活跃读写事务id，所以需要加上trx_sys-&gt;mutex这把大锁，为了减少其对性能的影响，关于readview有很多优化。例如，如果前后两个查询之间，没有产生新的读写事务，那么前一个查询创建的readview是可以被后一个查询复用的。</p>
<h2>垃圾回收Purge线程</h2>
<p>Purge线程主要做两件事，第一，数据页内标记的删除操作需要从物理上删除，为了提高删除效率和空间利用率，由后台Purge线程解析undolog定期批量清理。第二，当数据页上标记的删除记录已经被物理删除，同时undo所对应的记录已经能被所有事务看到，这个时候undo就没有存在的必要了，因此Purge线程还会把这些undo给truncate掉，释放更多的空间。</p>
<p>Purge线程有两种，一种是Purge Worker(<code>srv_worker_thread</code>), 另外一种是Purge Coordinator(<code>srv_purge_coordinator_thread</code>)，前者的主要工作就是从队列中取出Purge任务，然后清理已经被标记的记录。后者的工作除了清理删除记录外，还需要把Purge任务放入队列，唤醒Purge Worker线程，此外，它还要truncate undolog。</p>
<p>我们先来分析一下Purge Coordinator的流程。启动线程后，会进入一个大的循环，循环的终止条件是数据库关闭。在循环内部，首先是自适应的sleep，然后才会进入核心Purge逻辑。sleep时间与全局历史链表有关系，如果历史链表没有增长，且总数小于5000，则进入sleep，等待事务提交的时候被唤醒(<code>srv_purge_coordinator_suspend</code>)。退出循环后，也就是数据库进入关闭的流程，这个时候就需要依据参数innodb_fast_shutdown来确定在关闭前是否需要把所有记录给清除。接下来，介绍一下核心Purge逻辑。</p>
<ol>
<li>首先依据当前的系统负载来确定需要使用的Purge线程数(<code>srv_do_purge</code>)，即如果压力小，只用一个Purge Cooridinator线程就可以了。如果压力大，就多唤醒几个线程一起做清理记录的操作。如果全局历史链表在增加，或者全局历史链表已经超过<code>innodb_max_purge_lag</code>，则认为压力大，需要增加处理的线程数。如果数据库处于不活跃状态(<code>srv_check_activity</code>)，则减少处理的线程数。</li>
<li>如果历史链表很长，超过<code>innodb_max_purge_lag</code>，则需要重新计算delay时间(不超过<code>innodb_max_purge_lag_delay</code>)。如果计算结果大于0，则在后续的DML中需要先sleep，保证不会太快产生undo(<code>row_mysql_delay_if_needed</code>)。</li>
<li>从全局视图链表中，克隆最老的readview，所有在这个readview开启之前提交的事务所产生的undo都被认为是可以清理的。克隆之后，还需要把最老视图的创建者的id加入到<code>view-&gt;descriptors</code>中，因为这个事务修改产生的undo，暂时还不能删除(<code>read_view_purge_open</code>)。</li>
<li>从undo segment的最小堆中，找出最早提交事务的undolog(<code>trx_purge_get_rseg_with_min_trx_id</code>)，如果undolog标记过delete_mark(表示有记录删除操作)，则把先关undopage信息暂存在purge_sys_t中(<code>trx_purge_read_undo_rec</code>)。</li>
<li>依据purge_sys_t中的信息，读取出相应的undo，同时把相关信息加入到任务队列中。同时更新扫描过的指针，方便后续truncate undolog。</li>
<li>循环第4步和第5步，直到全局历史链表为空，或者接下到view-&gt;low_limit_no，即最老视图创建时已经提交的事务，或者已经解析的page数量超过<code>innodb_purge_batch_size</code>。</li>
<li>把所有的任务都放入队列后，就可以通知所有Purge Worker线程(如果有的话)去执行记录删除操作了。删除记录的核心逻辑在函数<code>row_purge_record_func</code>中。有两种情况，一种是数据记录被删除了，那么需要删除所有的聚集索引和二级索引(<code>row_purge_del_mark</code>)，另外一种是二级索引被更新了(总是先删除+插入新记录)，所以需要去执行清理操作。</li>
<li>在所有提交的任务都已经被执行完后，就可以调用函数<code>trx_purge_truncate</code>去删除update undo(insert undo在事务提交后就被清理了)。每个undo segment分别清理，从自己的histrory list中取出最早的一个undo，进行truncate(<code>trx_purge_truncate_rseg_history</code>)。truncate中，最终会调用<code>fseg_free_page</code>来清理磁盘上的空间。</li>
</ol>
<h2>事务的复活</h2>
<p>在奔溃恢复后，也就是所有的前滚redo都应用完后，数据库需要做undo回滚，至于哪些事务需要提交，哪些事务需要回滚，这取决于undolog和binlog的状态。启动阶段，事务相关的代码逻辑主要在函数<code>trx_sys_init_at_db_start</code>中，简单分析一下。</p>
<ol>
<li>首先创建管理undo segment的最小堆，堆中的元素是每个undo segment提交最早的事务id和相应undo segment的指针，也就是说通过这个元素可以找到这个undo segment中最老的未被Purge的undo。通过这个最小堆，可以找到所有undo segment中最老未被Purge的undo，方便Purge线程操作。</li>
<li>创建全局的活跃读写事务id数组。主要是给readview使用。</li>
<li>初始化所有的undo segment。主要是从磁盘读取undolog的内容，构建内存中的undo slot和undo segment，同时也构建每个undo segment中的history list，因为如果是fast shutdown，被标记为删除的记录可能还没来得及被彻底清理。此外，也构建每个undo segment中的inset_undo_list和update_undo_list，理论上来说，如果数据库关闭的时候所有事务都正常提交了，这两个链表都为空，如果数据库非正常关闭，则链表非空(<code>trx_undo_mem_create_at_db_start</code>, <code>trx_rseg_mem_create</code>)。</li>
<li>从系统页里面读取max_trx_id，然后加上TRX_SYS_TRX_ID_WRITE_MARGIN来保证trx_id不会重复，即使在很极端的情况下。</li>
<li>遍历所有的undo segment，针对每个undo segment，分别遍历inset_undo_list和update_undo_list，依据undo的状态来复活事务。</li>
<li>insert/update undo的处理逻辑：如果undolog上的状态是<code>TRX_UNDO_ACTIVE</code>，则事务也被设置为<code>TRX_STATE_ACTIVE</code>，如果undolog上的状态是<code>TRX_UNDO_PREPARED</code>，则事务也被设置为<code>TRX_UNDO_PREPARED</code>(如果force_recovery不为0，则设置为<code>TRX_STATE_ACTIVE</code>)。如果undolog状态是<code>TRX_UNDO_CACHED</code>,<code>TRX_UNDO_TO_FREE</code>,<code>TRX_UNDO_TO_PURGE</code>，那么都任务事务已经提交了(<code>trx_resurrect_insert</code>和<code>trx_resurrect_update</code>)。</li>
<li>除了从undolog中复活出事务的状态信息，还需要复活出当前的锁信息(<code>trx_resurrect_table_locks</code>)，此外还需要把事务trx_t加入到rw_trx_list中。</li>
<li>所有事务信息复活后，InnoDB会做个统计，告诉你有多少undo需要做，因此可以在错误日志中看到类似的话: InnoDB: 120 transaction(s) which must be rolled back or cleaned up. InnoDB: in total 20M row operations to undo。</li>
<li>如果事务中操作了数据字典，比如创建删除表和索引，则这个事务会在奔溃恢复结束后直接回滚，这个是个同步操作，会延长奔溃恢复的时间(<code>recv_recovery_from_checkpoint_finish</code>)。如果事务中没有操作数据字典，则后台会开启一个线程，异步回滚事务，所以我们常常发现，在数据库启动后，错误日志里面依然会有很多事务正在回滚的信息。</li>
</ol>
<h2>事务运维相关命令和参数</h2>
<ol>
<li>首先介绍一下information_schema中的三张表: innodb_trx, innodb_locks和innodb_lock_waits。由于这些表几乎需要查询所有事务子系统的核心数据结构，为了减少查询对系统性能的影响，InnoDB预留了一块内存，内存里面存了相关数据的副本，如果两次查询的时间小于0.1秒(<code>CACHE_MIN_IDLE_TIME_US</code>)，则访问的都是同一个副本。如果超过0.1秒，则这块内存会做一次更新，每次更新会把三张表用到的所有数据统一更新一遍，因为这三张表经常需要做表连接操作，所以一起更新能保证数据的一致性。这里简单介绍一下innodb_trx表中的字段，另外两张表涉及到事物锁的相关信息，由于篇幅限制，后续有机会在介绍。
trx_id: 就是trx_t中的事务id，如果是只读事务，这个id跟trx_t的指针地址有关，所以可能是一个很大的数字(<code>trx_get_id_for_print</code>)。
trx_weight: 这个是事务的权重，计算方法就是undolog数量加上事务已经加上锁的数量。在事务回滚的时候，优先选择回滚权重小的事务，有非事务引擎参与的事务被认为权重是最大的。
trx_rows_modified：这个就是当前事务已经产生的undolog数量，每更新一条记录一次，就会产生一条undo。
trx_concurrency_tickets: 每次这个事务需要进入InnoDB层时，这个值都会减一，如果减到0，则事务需要等待(压力大的情况下)。
trx_is_read_only: 如果是以<code>start transaction read only</code>启动事务的，那么这个字段是1，否则为0。
trx_autocommit_non_locking: 如果一个事务是一个普通的select语句(后面没有跟for update, share lock等)，且当时的autocommit为1，则这个字段为1，否则为0。
trx_state: 表示事务当前的状态，只能有<code>RUNNING</code>, <code>LOCK WAIT</code>, <code>ROLLING BACK</code>, <code>COMMITTING</code>这几种状态, 是比较粗粒度的状态。
trx_operation_state: 表示事务当前的详细状态，相比于trx_state更加详细，例如有<code>rollback to a savepoint</code>, <code>getting list of referencing foreign keys</code>, <code>rollback of internal trx on stats tables</code>, <code>dropping indexes</code>等。</li>
<li>与事务相关的undo参数
innodb_undo_directory: undo文件的目录，建议放在独立的一块盘上，尤其在经常有大事务的情况下。
innodb_undo_logs: 这个是定义了undo segment的个数。在给读写事务分配undo segment的时候，拿这个值去做轮训分配。
Innodb_available_undo_logs: 这个是一个status变量，在启动的时候就确定了，表示的是系统上分配的undo segment。举个例子说明其与innodb_undo_logs的关系：假设系统初始化的时候innodb_undo_logs为128，则在文件上一定有128个undo segment，Innodb_available_undo_logs也为128，但是启动起来后，innodb_undo_logs动态被调整为100，则后续的读写事务只会使用到前100个回滚段，最后的20多个不会使用。
innodb_undo_tablespaces: 存放undo segment的物理文件个数，文件名为undoN，undo segment会比较均匀的分布在undo tablespace中。</li>
<li>与Purge相关的参数
innodb_purge_threads: Purge Worker和Purge Coordinator总共的个数。在实际的实现中，使用多少个线程去做Purge是InnoDB根据实时负载进行动态调节的。
innodb_purge_batch_size: 一次性处理的undolog的数量，处理完这个数量后，Purge线程会计算是否需要sleep。
innodb_max_purge_lag: 如果全局历史链表超过这个值，就会增加Purge Worker线程的数量，也会使用sleep的方式delay用户的DML。
innodb_max_purge_lag_delay: 这个表示通过sleep方式delay用户DML最大的时间。</li>
<li>与回滚相关的参数
innodb_lock_wait_timeout: 等待行锁的最大时间，如果超时，则会滚当前语句或者整个事务。发生回滚后返回类似错误：Lock wait timeout exceeded; try restarting transaction。
innodb_rollback_on_timeout: 如果这个参数为true，则当发生因为等待行锁而产生的超时时，回滚掉整个事务，否则只回滚当前的语句。这个就是隐式回滚机制。主要是为了兼容之前的版本。</li>
</ol>
<h2>总结</h2>
<p>本文简单介绍了InnoDB事务子系统的几个核心模块，在MySQL 5.7上，事务模块还有很多特性，例如高优先级事务，事务对象池等。与事务相关的还有事务锁系统，由于篇幅限制，本文不介绍，详情可以参考本期月报的这篇。此外，在阿里云最新发布的POLARDB for MySQL的版本中，由于涉及到共享存储架构，我们对事务子系统又进行了大量的改造，后续的月报会详细介绍。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;IO子系统.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="MySQL&#32;·&#32;引擎特性&#32;·&#32;InnoDB&#32;同步机制.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4362c3d99c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
