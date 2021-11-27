<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>全面了解 JDK 线程池实现原理.md</title>
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

                    <a class="current-tab" href="全面了解&#32;JDK&#32;线程池实现原理.md">全面了解 JDK 线程池实现原理.md</a>
                    

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
                        <div><h1>全面了解 JDK 线程池实现原理</h1>
<h3>前言</h3>
<p>线程池，顾名思义就是存放线程的池子，池子中存放了很多可复用的线程。使用线程池，具有以下优点：</p>
<ul>
<li>通过可复用的线程，避免线程频繁创建和销毁，降低系统资源消耗</li>
<li>提高系统任务处理速度</li>
<li>增加线程的可管理性，使用线程池可以对线程进行统一监控、分配等</li>
</ul>
<h3>基础构造</h3>
<p>回顾 JDK 线程池中有核心线程和非核心线程之分，当线程数未达到<strong>核心线程数</strong>时，添加一个任务就会创建一个线程，当达到核心线程数时，为了控制线程的数量，多余的任务将会放入<strong>阻塞队列</strong>中，当队列也满了的话，此时为了提高系统的执行任务的效率，便会创建非核心线程，当然非核心线程也不能无限制创建，当达到<strong>最大线程数</strong>时，便会执行<strong>拒绝策略</strong>。</p>
<p>这里有核心线程和非核心线程，其含义有：</p>
<ul>
<li>核心和非核心只是线程在不同阶段的称呼，两者的本质是完全一致的</li>
<li>区分核心非核心主要是为了控制线程的数量</li>
</ul>
<p>因此从上面我们能够归纳出一个线程池的构造结构有核心线程数、阻塞队列、最大线程数、拒绝策略，通过代码可以表示为：</p>
<pre><code>public class LimynlThreadPool{

    /**
     * 线程池名称
     */
    private String name;

    /**
     * 核心线程数
     */
    private int coreSize;

    /**
     * 最大线程数
     */
    private int maxSize;

    /**
     * 阻塞队列
     */
    private BlockingQueue&lt;Runnable&gt; taskQueue;

    /**
     * 拒绝策略
     */
    private RejectPolicy rejectPolicy;

    public LimynlThreadPoolExecutor(String name, int coreSize, int maxSize, BlockingQueue&lt;Runnable&gt; taskQueue, RejectPolicy rejectPolicy) {
        this.name = name;
        this.coreSize = coreSize;
        this.maxSize = maxSize;
        this.taskQueue = taskQueue;
        this.rejectPolicy = rejectPolicy;
    }
}
</code></pre>
<p>继续分析，对于普通用户来说使用线程池的目的就是将需要执行的任务提交到线程池中去执行，因此我们还需要定义一个提交任务的入口，为了实现面向接口编程，我们抽象一个接口：</p>
<pre><code>public interface Executor {
    /**
     * 任务执行入口
     */
    void execute(Runnable task);
}
</code></pre>
<h3>执行无返回值任务</h3>
<p>从上面分析可知，我们的线程池的的整体流程可化分为两大部分：即任务执行部分、线程创建部分。</p>
<h4>任务执行部分</h4>
<p>对于任务执行部分主要流程为：</p>
<ul>
<li>如果运行的线程数（runningCount）小于核心线程数，则创建一个线程来执行任务</li>
<li>如果达到核心线程数，则将任务提交到阻塞队列</li>
<li>如果添加队列失败，即队列已满，创建非核心线程来执行任务</li>
<li>如果线程数达到最大线程数，则执行拒绝策略</li>
</ul>
<p>注意这里线程数量计数器 runningCount 为了保证多线程环境下的原子性和可见性，我们可以使用 AtomicInteger 来修饰，因为 AtomicInteger 底层就是使用 CAS 来保证原子性，使用 volatile 来保证可见性。</p>
<p>此时我们的线程池为：</p>
<pre><code>public class LimynlThreadPool implements Executor {

    private String name;
    private int coreSize;
    private int maxSize;
    private BlockingQueue&lt;Runnable&gt; taskQueue;
    private RejectPolicy rejectPolicy;

    /**
     * 当前正在运行的线程数(底层采用 CAS+volatile 实现)
     */
    private AtomicInteger runningCount = new AtomicInteger(0);

    // 线程计数器
    private AtomicInteger threadCounter = new AtomicInteger(0);

    public LimynlThreadPoolExecutor(String name, int coreSize, int maxSize, BlockingQueue&lt;Runnable&gt; taskQueue, RejectPolicy rejectPolicy) {
        this.name = name;
        this.coreSize = coreSize;
        this.maxSize = maxSize;
        this.taskQueue = taskQueue;
        this.rejectPolicy = rejectPolicy;
    }

    @Override
    public void execute(Runnable task) {
        // 线程池的线程总数
        int count = runningCount.get();
        // 如果正在运行的线程数小于核心线程数，直接创建一个线程
        if (count &lt; coreSize) {
            if (addWorker(task, true)) {
                return;
            }
        }

        // 如果达到核心线程数，则将任务提交到阻塞队列
        if(!taskQueue.offer(task)){
            // 如果队列已满，创建非核心线程来执行任务
            if (!addWorker(task, false)) {
                // 线程数达到最大线程数，执行拒绝策略
                rejectPolicy.reject(task, this);
            }
        }
    }
}
</code></pre>
<h4>线程创建部分</h4>
<p>对于线程创建部分主要是看线程池中创建的线程是否达到了最大线程数，如果达到了最大线程数直接返回，如果没有达到最大线程数，直接创建线程，并且执行新任务，以后从阻塞队列中获取任务执行。</p>
<pre><code>private boolean addWorker(Runnable newTask, boolean isCore) {
    while(true){
        int count = runningCount.get();
        int maxNum = isCore ? coreSize : maxSize;
        // 如果当前线程数量大于核心线程数或者非核心线程数，直接返回执行下一步
        if (count &gt;= maxNum) {
            return false;
        }

        // 原子修改线程数，如果失败，说明其他线程在修改，通过外层的 while 实现重试
        if (runningCount.compareAndSet(count, count + 1)) {
            String threadName = name + threadCounter.incrementAndGet();
            // 创建线程并启动
            new Thread(() -&gt; {
                System.out.println(&quot;thread name : &quot; + Thread.currentThread().getName());
                Runnable task = newTask;
                // 第一次执行完新任务后，以后直接从阻塞队列中获取任务并执行，
                // 如果阻塞队列中没有任务，将会一直阻塞到这里，直到有任务可执行为止
                // 注意：从这里可以看出来对于线程池来说，为什么使用的是阻塞队列而不是普通队列了
                while (task != null || (task = getTask()) != null) {
                    try {
                        // 执行真正的任务
                        task.run();
                    } finally {
                        // 任务执行完成，置为 null
                        task = null;
                    }
                }
            }, threadName).start();
            break;
        }
    }
    return true;
}

private Runnable getTask() {
    try {
        // 一直阻塞线程知道取到任务为止，维持核心线程的存活
        return taskQueue.take();
    } catch (InterruptedException e) {
        // 如果线程中断，说明当前线程已终止，线程池中的总数量应该减 1
        runningCount.decrementAndGet();
        return null;
    }
}
</code></pre>
<h4>拒绝策略</h4>
<p>到这里一个线程池的雏形已经构建出来了，但是对于线程池任务队列已经满了，并且最大线程数也达到了最大值，因此再次提交的任务需要执行拒绝策略，常见的拒绝策略有：直接抛弃、调用线程自己处理、抛出异常、丢弃队列中最古老的任务等等。这里我们以直接抛弃为例，看看如果自定义拒绝策略。</p>
<p>首先定义线程池的公共接口：</p>
<pre><code>public interface RejectPolicy {
    void reject(Runnable task, LimynlThreadPool limynlThreadPool);
}
</code></pre>
<p>实现自定义拒绝策略：</p>
<pre><code>public class DiscardRejectPolicy implements RejectPolicy {
    @Override
    public void reject(Runnable task, LimynlThreadPool limynlThreadPool) {
        System.out.println(&quot;discard one task&quot;);
    }
}
</code></pre>
<p>到此我们基于 Runnable 实现不带返回值的任务的线程池，下面通过测试用例验证。</p>
<pre><code>public class Main {

    public static void main(String[] args) {
        Executor threadPool = new LimynlThreadPool(&quot;test&quot;, 5, 8, new ArrayBlockingQueue&lt;&gt;(5), new DiscardRejectPolicy());
        AtomicInteger counter = new AtomicInteger(0);

        IntStream.range(0, 15).forEach(index -&gt; threadPool.execute(() -&gt; {
            try {
                Thread.sleep(1000);
                System.out.println(&quot;running: &quot; + System.currentTimeMillis() + &quot;: &quot; + counter.incrementAndGet());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));
    }
}
</code></pre>
<p>执行结果为：</p>
<pre><code>thread name : test1
thread name : test6
thread name : test7
discard one task
thread name : test5
thread name : test4
thread name : test3
thread name : test2
discard one task
thread name : test8
running: 1601343696818: 1
running: 1601343696818: 5
running: 1601343696818: 7
running: 1601343696818: 3
running: 1601343696818: 6
running: 1601343696818: 2
running: 1601343696818: 4
running: 1601343696818: 8
running: 1601343697819: 9
running: 1601343697819: 13
running: 1601343697819: 10
running: 1601343697819: 12
running: 1601343697819: 11
</code></pre>
<h3>执行有返回值任务</h3>
<p>从上一节知道，我们使用 Runnable 实现了无返回值的任务线程池执行能力。但是有时我们需要获取任务的执行结果。因此当主线程将任务提交到线程池中后，需要等待任务执行完毕后才能获取到任务的结果。因此我们应该清楚，当任务未执行或者还在执行过程中，当前线程如果需要获取该任务的执行结果，需要阻塞，直到任务执行完成。 对于无返回值任务的执行，我们使用的 Runnable，对于有返回值任务，我们使用 Callable 实现，因此对于线程执行接口，我们需要进行改造，以至于能够返回任务的执行结果。</p>
<pre><code>public interface FutureExecutor extends Executor {
    // 将任务的执行结果包装到 Future 中
    &lt;T&gt; Future&lt;T&gt; submit(Callable&lt;T&gt; task);
}

public interface Future&lt;T&gt; {
    /**
     * 获取任务的结果
     */
    T get();
}
</code></pre>
<h4>任务定义</h4>
<p>接下来我们需要一种新任务，这种任务既能够执行，又能够返回执行结果，因此我们可以同时实现 Runnabl、Future 接口，为了表示任务所处的阶段，我们需要定义任务的状态，因此新任务的定义如下：</p>
<pre><code>public class FutureTask&lt;T&gt; implements Runnable, Future {
    /**
     * 任务执行状态：0 未开始 1 正常完成 2 异常完成
     */
    private static final int NEW = 0;
    private static final int FINISHED = 1;
    private static final int EXCEPTION = 2;

    /**
     * 真正需要执行的任务
     */
    private Callable&lt;T&gt; task;

    // 通过原子类去更新线程状态
    private AtomicInteger state = new AtomicInteger(NEW);

    /**
     * 保存任务的执行结果
     */
    private Object result;

    public FutureTask(Callable&lt;T&gt; task) {
        this.task = task;
    }

    @Override
    public T get() {
        return null;
    }

    @Override
    public void run() {
    }
}
</code></pre>
<p>因此到这里我们的准备工作都完成了，接下里看如何执行任务，以及如何获取任务执行结果。</p>
<h4>任务执行部分</h4>
<ul>
<li>对于线程的执行部分首先我们需要检测线程是否是新建状态，如果不是直接返回</li>
<li>如果是新建任务直接执行任务</li>
<li>原子更新当前任务状态</li>
<li>判断调用者是否为空，如果不为空，则唤醒</li>
</ul>
<pre><code>@Override
public void run() {
    // 任务不是新建状态，说明执行过了
    if (state.get() != NEW) {
        return;
    }
    try {
        // 执行真正的任务
        T t = task.call();

        /**
         * 原子更新任务状态
         */
        if (state.compareAndSet(NEW, FINISHED)) {
            this.result = t;
            // 检查是否有调用者
            finish();
        }
    } catch (Exception e) {
        // 任务异常，直接返回异常 
        if (state.compareAndSet(NEW, EXCEPTION)) {
            this.result = e;
            finish();
        }
    }
}

private void finish() {
    for (Thread c; (c = caller.get()) != null; ) {
        if (caller.compareAndSet(c, null)) {
            // 使用 unpark 唤醒调用线程
            LockSupport.unpark (c);
        }
    }
}   
</code></pre>
<h4>获取任务执行结果</h4>
<p>获取执行结果主要流程为：</p>
<ul>
<li>如果任务执行过，直接返回结果</li>
<li>如果任务执行过程发生异常，直接抛出异常，此时异常将会抛到子线程外</li>
<li>如果任务处于执行过程中，需要判断调用者线程是否需要阻塞</li>
</ul>
<pre><code>@Override
public T get() {
    int s = state.get();
    // 如果线程还在执行，需要判断
    if (s == NEW) {
        // 为了判断当前调用者是否已经阻塞，我们需要一个标识
        boolean flag = false;
        for (; ; ) {
            s = state.get();
            // 说明当前任务执行完成，跳出循环
            if (s &gt; NEW) {
                break;
            } else if (!flag) {
                marked = caller.compareAndSet(null, Thread.currentThread());
            } else {
                // 将当前调用者线程阻塞，直到任务执行完成，被唤醒
                LockSupport.park();
            }
        }
    }

    // 如果线程执行过，直接返回结果
    if (s == FINISHED) {
        return (T) result;
    }

    throw new RuntimeException((Throwable) result);
}
</code></pre>
<h4>线程提交入口</h4>
<p>上面我们把具有执行返回值的任务整体流程梳理完成，接下来就是如何吧任务提交给线程池，以及如何把我们定义的任务包装成具有执行能力和返回结果。</p>
<p>为了实现之前代码的复用，我们直接继承 LimynlThreadPool 并且实现 FutureExecutor：</p>
<pre><code>public class LimynlThreadPoolFuture extends LimynlThreadPool implements FutureExecutor {

    public LimynlThreadPoolFutureExecutor(String name, 
                                          int coreSize, 
                                          int maxSize, 
                                          BlockingQueue&lt;Runnable&gt; taskQueue, 
                                          RejectPolicy rejectPolicy) {
        super(name, coreSize, maxSize, taskQueue, rejectPolicy);
    }

    @Override
    public &lt;T&gt; Future&lt;T&gt; submit(Callable&lt;T&gt; task) {
        // 将任务进行包装
        FutureTask&lt;T&gt; futureTask = new FutureTask&lt;&gt;(task);
        // 将任务提交到线程池
        execute(futureTask);
        // 返回 Future，通过访问 get 方法就能够获取任务的执行结果
        return futureTask;
    }
}
</code></pre>
<p>接下来我们验证我们的代码：</p>
<pre><code>public class Main {

    public static void main(String[] args) {
        FutureExecutor executor = new LimynlThreadPoolFutureExecutor(&quot;test&quot;, 2, 4,
                new ArrayBlockingQueue&lt;&gt;(6), new DiscardRejectPolicy());
        List&lt;Future&lt;Integer&gt;&gt; list = new ArrayList&lt;&gt;();
        IntStream.range(0, 10).forEach(i -&gt; {
            Future&lt;Integer&gt; future = executor.submit(() -&gt; {
                Thread.sleep(1000);
                System.out.println(&quot;running: &quot; + i);
                return i;
            });

            list.add(future);
        });

        list.forEach(item -&gt; System.out.println(item.get()));
    }
}
</code></pre>
<p>运行结果：</p>
<pre><code>thread name : core_test1
thread name : core_test2
thread name : test3
thread name : test4
running: 0
0
running: 1
1
running: 8
running: 9
running: 2
2
running: 3
3
running: 4
4
running: 5
5
running: 6
6
running: 7
7
8
9
</code></pre>
<h3>回顾</h3>
<p>以上我们实现了基于 Runnable 实现不带返回值的任务，基于 Callable 实现带返回值的任务，通过原子类实现状态更新。整个过程也是比较好理解的，整体框架原型其实就是 JDK 线程池 ThreadPoolExecutor 的大体流程。通过手写线程池，回头再去看看线程池源码相信会有不一样的收获。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="从SpringCloud开始，聊微服务架构.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="分布式一致性理论与算法.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4363dacfb0645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
