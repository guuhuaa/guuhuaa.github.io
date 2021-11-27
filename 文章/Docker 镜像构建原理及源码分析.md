<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>Docker 镜像构建原理及源码分析.md</title>
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

                    <a class="current-tab" href="Docker&#32;镜像构建原理及源码分析.md">Docker 镜像构建原理及源码分析.md</a>
                    

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
                        <div><h1>Docker 镜像构建原理及源码分析</h1>
<h3>Docker 架构</h3>
<p>这里我们先从宏观上对 <code>Docker</code> 有个大概的认识，就像我[之前]提到的它整体上是个 C/S 架构；我们平时使用的 <code>docker</code> 命令就是它的 CLI 客户端，而它的服务端是 <code>dockerd</code> 在 Linux 系统中，通常我们是使用 <code>systemd</code> 进行管理，所以我们可以使用 <code>systemctl start docker</code> 来启动服务。（但是请注意，<code>dockerd</code> 是否能运行与 <code>systemd</code> 并无任何关系，你可以像平时执行一个普通的二进制程序一样，直接通过 <code>dockerd</code> 来启动服务，注意需要 root 权限）</p>
<p>实际上也就是</p>
<p><img src="assets/engine-components-flow.png" alt="Docker 架构" /></p>
<p>(图片来源：docker overview)</p>
<p><code>docker</code> CLI 与 <code>dockerd</code> 的交互是通过 rest API 来完成的，当我们执行 <code>docker version</code> 的时候过滤 API 可以看到如下输出：</p>
<pre><code>/ # docker version  |grep API
 API version:       1.40
  API version:      1.40 (minimum version 1.12)
</code></pre>
<p>上面一行是 <code>docker</code> CLI 的 API 版本，下面则代表了 <code>dockerd</code> 的 API 版本，它的后面还有个括号，是因为 Docker 具备了很良好的兼容性，这里表示它最小可兼容的 API 版本是 1.12 。</p>
<p>对于我们进行 C/S 架构的项目开发而言，一般都是 API 先行, 所以我们先来看下 API 的部分。</p>
<p>当然，本次 Chat 的主体是构建系统相关的，所以我们就直接来看构建相关的 API 即可。</p>
<p>接下来会说 CLI，代码以 v19.03.0-rc2-4-ga63faebc 为准。</p>
<p>最后说服务端 Dockerd 。</p>
<h3>API</h3>
<p>Docker 官方在每个版本正式发布之后，都会将 API 文档发布出来，在线地址是 https://docs.docker.com/engine/api/v1.39/#operation/ImageBuild 但由于现在 19.03 还未发布，所以 1.40 版本的 API 文档也尚未正式发布。</p>
<p>1.39 和 1.40 中，关于镜像构建部分的 API 其实没太大变化，所以直接参考 1.39 版本的 API 文档看也可以。或者我们也可以自行构建 API 文档。</p>
<p>首先 clone Docker 的源代码仓库, 进入项目仓库内执行 <code>make swagger-docs</code> 即可在启动一个容器同时将端口暴露至本地的 <code>9000</code> 端口， 你可以直接通过 <a href="http://127.0.0.1:9000/">http://127.0.0.1:9000</a> 访问本地的 API 文档。</p>
<pre><code>(MoeLove) ➜  git clone https://github.com/docker/engine.git docker
(MoeLove) ➜  cd docker
(MoeLove) ➜  docker git:(master) git checkout -b v19.03.0-rc2 v19.03.0-rc2
(MoeLove) ➜  docker git:(v19.03.0-rc2) make swagger-docs
API docs preview will be running at http://localhost:9000
</code></pre>
<p>打开 <a href="http://127.0.0.1:9000/#operation/ImageBuild">http://127.0.0.1:9000/#operation/ImageBuild</a> 这个地址就可以看到 1.40 版本的构建镜像所需的 API 了。我们对此 API 进行下分析。</p>
<h4>请求地址和方法</h4>
<p>接口地址是 <code>/v1.40/build</code> 方法是 <code>POST</code></p>
<p>我们可以使用一个较新版本的 <code>curl</code> 工具来验证下此接口（需要使用 <code>--unix-socket</code> 连接 Docker 监听的 UNIX Domain Socket ）</p>
<p><code>/var/run/docker.sock</code> 这是默认情况下 <code>dockerd</code> 所监听的地址，当然你也可以给 <code>dockerd</code> 传递 <code>--host</code> 参数用于监听 HTTP 端口或者其他路径的 unix socket .</p>
<pre><code>/ # curl -X POST --unix-socket /var/run/docker.sock  localhost/v1.40/build 
{&quot;message&quot;:&quot;Cannot locate specified Dockerfile: Dockerfile&quot;}
</code></pre>
<p>从上面的输出我们可以看到，我们确实访问到了该接口，同时该接口的响应是提示需要 <code>Dockerfile</code> .</p>
<h4>请求体</h4>
<blockquote>
<p>A tar archive compressed with one of the following algorithms: identity (no compression), gzip, bzip2, xz. string</p>
</blockquote>
<p>请求体是一个 <code>tar</code> 归档文件，可选择无压缩、<code>gzip</code>、<code>bzip2</code>、<code>xz</code> 压缩等形式。关于这几种压缩格式就不再展开介绍了，但值得注意的是 <strong>如果使用了压缩，则传输体积会变小，即网络消耗会相应减少。但压缩/解压缩需要耗费 CPU 等计算资源</strong> 这在我们对大规模镜像构建做优化时是个值得权衡的点。</p>
<h4>请求头</h4>
<p>因为要发送的是个 <code>tar</code> 归档文件，<code>Content-type</code> 默认是 <code>application/x-tar</code> 。</p>
<p>另一个会发送的头是 <code>X-Registry-Config</code>，这是一个由 Base64 编码后的 Docker Registry 的配置信息，内容与 <code>$HOME/.docker/config.json</code> 中的 <code>auths</code> 内的信息一致。</p>
<p>这些配置信息，在你执行 <code>docker login</code> 后会自动写入到 <code>$HOME/.docker/config.json</code> 文件内的。这些信息被传输到 <code>dockerd</code> 在构建过程中作为拉取镜像的认证信息使用。</p>
<h3>请求参数</h3>
<p>最后就是请求参数了，参数有很多，通过 <code>docker build --help</code> 基本都可以看到对应含义的，这里不再一一展开了，后面会有一些关键参数的介绍。</p>
<h4>小结</h4>
<p>上面我们介绍了 <code>Docker</code> 构建镜像相关的 API，我们可以通过在线地址 https://docs.docker.com/engine/api/v1.39/#operation/ImageBuild 访问旧版本的 API，待新版本发布后，就可以访问新版本 API 文档了。或者通过源码仓库，自己来构建一个本地的 API 文档服务，使用浏览器进行访问。</p>
<p>通过 API 我们也知道了该接口所需的请求体是一个 <code>tar</code> 归档文件（可选择压缩算法进行压缩），同时它的请求头中会携带用户在镜像仓库中的认证信息。</p>
<p>这提醒我们， <strong>如果在使用远程 Dockerd 构建时，请注意安全，尽量使用 tls 进行加密，以免数据泄漏。</strong></p>
<h3>CLI</h3>
<p>API 已经介绍完了，我们来看下 <code>docker</code> CLI，在我们前两次的 Chat中，我们聊过现在 Docker 中有两个构建系统，一个是 v1 版本的 <code>builder</code> 另一个是 v2 版本的即 <code>buildkit</code> 我们来分别深入源码来看看在构建镜像时，他们各自的行为吧。</p>
<h4>准备代码</h4>
<p>CLI 的代码仓库在 https://github.com/docker/cli 本次 Chat 的代码以 <code>v19.03.0-rc2-4-ga63faebc</code> 为准。</p>
<p>通过以下步骤使用此版本的代码：</p>
<pre><code>(MoeLove) ➜  git clone https://github.com/docker/cli.git
(MoeLove) ➜  cd cli
(MoeLove) ➜  cli git:(master) git checkout -b v19.03 v19.03.0-rc2-4-ga63faebc
</code></pre>
<h4>逐步分解</h4>
<p><code>docker</code> 是我们所使用的客户端工具，用于与 <code>dockerd</code> 进行交互。关于构建相关的部分， 我们所熟知的便是 <code>docker build</code> 或者是 <code>docker image build</code>，在 19.03 中新增的是 <code>docker builder build</code> ，但其实他们都是同一个只是做了个 alias 罢了：</p>
<pre><code class="language-go">// cmd/docker/docker.go#L231

if v, ok := aliasMap[&quot;builder&quot;]; ok {
    aliases = append(aliases,
        [2][]string{{&quot;build&quot;}, {v, &quot;build&quot;}},
        [2][]string{{&quot;image&quot;, &quot;build&quot;}, {v, &quot;build&quot;}},
    )
}
</code></pre>
<p>真正的入口函数其实在 <code>cli/command/image/build.go</code> ；区分如何调用的逻辑如下：</p>
<pre><code class="language-go">func runBuild(dockerCli command.Cli, options buildOptions) error {
    buildkitEnabled, err := command.BuildKitEnabled(dockerCli.ServerInfo())
    if err != nil {
        return err
    }
    if buildkitEnabled {
        return runBuildBuildKit(dockerCli, options)
    }
    // 省略掉了对于 builder 的实际逻辑
}
</code></pre>
<p>这里就是判断下是否支持 <code>buildkit</code></p>
<pre><code class="language-go">// cli/command/cli.go#L151
func BuildKitEnabled(si ServerInfo) (bool, error) {
    buildkitEnabled := si.BuildkitVersion == types.BuilderBuildKit
    if buildkitEnv := os.Getenv(&quot;DOCKER_BUILDKIT&quot;); buildkitEnv != &quot;&quot; {
        var err error
        buildkitEnabled, err = strconv.ParseBool(buildkitEnv)
        if err != nil {
            return false, errors.Wrap(err, &quot;DOCKER_BUILDKIT environment variable expects boolean value&quot;)
        }
    }
    return buildkitEnabled, nil
}
</code></pre>
<p>当然，从这里可以得到两个信息：</p>
<ul>
<li>通过 <code>dockerd</code> 的配置可开启 <code>buildkit</code> 。在 <code>/etc/docker/daemon.json</code> 中添加如下内容，并重启 <code>dockerd</code> 即可：</li>
</ul>
<pre><code class="language-json">{
  &quot;features&quot;: {
    &quot;buildkit&quot;: true
  }
}
</code></pre>
<ul>
<li>在 <code>docker</code> CLI 上也可开启 <code>buildkit</code> 的支持，并且 CLI 的配置可覆盖服务端配置:</li>
</ul>
<p>通过 <code>export DOCKER_BUILDKIT=1</code> 即可开启 <code>buildkit</code> 的支持，设置为 0 则关闭（0/false/f/F 之类的也都是相同的结果）</p>
<p>从上面的介绍也看到了，对于原本默认的 builder 而言， 入口逻辑在 <code>runBuild</code> 中， 而对于使用 buildkit 的则是 <code>runBuildBuildKit</code> 接下来，我们对两者进行逐步分解。</p>
<h3>builder v1</h3>
<p>在 <code>runBuild</code> 函数中，大致经历了以下阶段：</p>
<h4>参数处理</h4>
<p>最开始的部分是一些对参数的处理和校验。</p>
<ul>
<li><strong>stream 和 compress 不可同时使用。</strong></li>
</ul>
<p>因为如果我们指定了 <code>compress</code> 的话，则 CLI 会使用 <code>gzip</code> 将构建上下文进行压缩，这样也就没法很好的通过 <code>stream</code> 的模式来处理构建的上下文了。</p>
<p>当然你也可能会想，从技术上来讲，压缩和流式没有什么必然的冲突，是可实现的。事实的确如此，如果从技术的角度上来讲两者并非完全不能一起存在，无非就是增加解压缩的动作。但是当开启 <code>stream</code> 模式，对每个文件都进行压缩和解压的操作那将会是很大的资源浪费，同时也增加了其复杂度，所以在 CLI 中便直接进行了限制，不允许同时使用 <code>compress</code> 和 <code>stream</code></p>
<ul>
<li><strong>不可同时使用 stdin 读取 Dockerfile 和 build context。</strong></li>
</ul>
<p>在进行构建时，如果我们将 <code>Dockerfile</code> 的名字传递为 <code>-</code> 时，表示从 <code>stdin</code> 读取其内容。</p>
<p>例如，某个目录下有三个文件 <code>foo</code> <code>bar</code> 和 <code>Dockerfile</code>，通过管道将 <code>Dockerfile</code> 的内容通过 <code>stdin</code> 传递给 <code>docker build</code></p>
<pre><code>(MoeLove) ➜  x ls
bar  Dockerfile  foo
(MoeLove) ➜  x cat Dockerfile | DOCKER_BUILDKIT=0 docker build -f - .
Sending build context to Docker daemon  15.41kB
Step 1/3 : FROM scratch
 ---&gt; 
Step 2/3 : COPY foo foo
 ---&gt; a2af45d66bb5
Step 3/3 : COPY bar bar
 ---&gt; cc803c675dd2
Successfully built cc803c675dd2
</code></pre>
<p>可以看到通过 <code>stdin</code> 传递 <code>Dockerfile</code> 的方式能成功的构建镜像。接下来我们尝试通过 <code>stdin</code> 将 <code>build context</code> 传递进去。</p>
<pre><code>(MoeLove) ➜  x tar -cvf x.tar foo bar Dockerfile 
foo                                                     
bar                         
Dockerfile
(MoeLove) ➜  x cat x.tar| DOCKER_BUILDKIT=0 docker build -f Dockerfile -
Sending build context to Docker daemon  10.24kB
Step 1/3 : FROM scratch
 ---&gt; 
Step 2/3 : COPY foo foo
 ---&gt; 09319712e220
Step 3/3 : COPY bar bar
 ---&gt; ce88644a7395
Successfully built ce88644a7395
</code></pre>
<p>可以看到通过 <code>stdin</code> 传递 <code>build context</code> 的方式也可以成功构建镜像。</p>
<p>但如果 <code>Dockerfile</code> 的名称与构建的上下文都指定为 <code>-</code> 即 <code>docker build -f - -</code> 时，会发生什么呢？</p>
<pre><code>(MoeLove) ➜  x DOCKER_BUILDKIT=0 docker build -f - -             
invalid argument: can't use stdin for both build context and dockerfile
</code></pre>
<p>就会报错了。所以， <strong>不能同时使用 stdin 读取 Dockerfile 和 build context</strong> 。</p>
<ul>
<li><strong>build context 支持四种行为。</strong></li>
</ul>
<pre><code class="language-go">switch {
case options.contextFromStdin():
    // 省略
case isLocalDir(specifiedContext):
    // 省略
case urlutil.IsGitURL(specifiedContext):
    // 省略
case urlutil.IsURL(specifiedContext):
    // 省略
default:
    return errors.Errorf(&quot;unable to prepare context: path %q not found&quot;, specifiedContext)
}
</code></pre>
<p>从 <code>stdin</code> 传入，上文已经演示过了，传递给 <code>stdin</code> 的是 <code>tar</code> 归档文件；</p>
<p>当然也可以是指定一个具体的 <code>PATH</code>，我们通常使用的 <code>docker build .</code> 便是这种用法；</p>
<p>或者可以指定一个 <code>git</code> 仓库的地址，CLI 会调用 <code>git</code> 命令将仓库 <code>clone</code> 至一个临时目录，进行使用；</p>
<p>最后一种是，给定一个 <code>URL</code> 地址，该地址可以是 <strong>一个具体的 Dockerfile 文件地址</strong> 或者是 <strong>一个 tar 归档文件的下载地址</strong> 。</p>
<p>这几种基本就是字面上的区别，至于 CLI 的行为差异，主要是最后一种，当 <code>URL</code> 地址是一个具体的 <code>Dockerfile</code> 文件地址，在这种情况下 <code>build context</code> 相当于只有 <code>Dockerfile</code> 自身，所以并不能使用 <code>COPY</code> 之类的指定，至于 <code>ADD</code> 也只能使用可访问的外部地址。</p>
<ul>
<li><strong>可使用 .dockerignore 忽略不需要的文件</strong></li>
</ul>
<p>我在之前的 Chat [高效构建 Docker 镜像的最佳实践] 中有分享过相关的内容。这里我们看看它的实现逻辑。</p>
<pre><code class="language-go">// cli/command/image/build/dockerignore.go#L13
func ReadDockerignore(contextDir string) ([]string, error) {
    var excludes []string

    f, err := os.Open(filepath.Join(contextDir, &quot;.dockerignore&quot;))
    switch {
    case os.IsNotExist(err):
        return excludes, nil
    case err != nil:
        return nil, err
    }
    defer f.Close()

    return dockerignore.ReadAll(f)
}
</code></pre>
<ul>
<li><code>.dockerignore</code> 是一个固定的文件名，并且需要放在 <code>build context</code> 的根目录下。类似前面提到的，使用一个 <code>Dockerfile</code> 文件的 URL 地址作为 <code>build context</code> 传入的方式，便无法使用 <code>.dockerignore</code> 。</li>
<li><code>.dockerignore</code> 文件可以不存在，但在读取的时候如果遇到错误，便会抛出错误。</li>
<li>通过 <code>.dockerignore</code> 将会过滤掉不希望加入到镜像内，或者过滤掉与镜像无关的内容。</li>
</ul>
<p>最后 CLI 会将 <code>build context</code> 中的内容经过 <code>.dockerignore</code> 过滤后，打包成为真正的 <code>build context</code> 即真正的构建上下文。这也是为什么有时候你发现自己明明在 <code>Dockerfile</code> 里面写了 <code>COPY xx xx</code> 但是最后没有发现该文件的情况。 很可能就是被 <code>.dockerignore</code> 给忽略掉了。</p>
<p>这样有利于优化 CLI 与 <code>dockerd</code> 之间的传输压力之类的。</p>
<ul>
<li><code>docker</code> CLI 还会去读取 <code>~/.docker/config.json</code> 中的内容。</li>
</ul>
<p>这与前面 API 部分所描述的内容基本是一致的。将认证信息通过 <code>X-Registry-Config</code> 头传递给 <code>dockerd</code> 用于在需要拉取镜像时进行身份校验。</p>
<ul>
<li><strong>调用 API 进行实际构建任务</strong></li>
</ul>
<p>当一切所需的校验和信息都准备就绪之后，则开始调用 <code>dockerCli.Client</code> 封装的 API 接口，将请求发送至 <code>dockerd</code>，进行实际的构建任务。</p>
<pre><code class="language-go">response, err := dockerCli.Client().ImageBuild(ctx, body, buildOptions)
if err != nil {
    if options.quiet {
        fmt.Fprintf(dockerCli.Err(), &quot;%s&quot;, progBuff)
    }
    cancel()
    return err
}
defer response.Body.Close()
</code></pre>
<p>到这里其实一次构建的过程中 CLI 所处理的流程就基本结束了，之后便是按照传递的参数进行进度的输出或是将镜像 ID 写入到文件之类的。 这部分就不进行展开了。</p>
<h4>小结</h4>
<p>整个过程大致如下图：</p>
<p><img src="assets/6a69dde0-933a-11e9-8825-e7da71af5ddb.jpg" alt="docker builder 处理流程" /></p>
<p>从入口函数 <code>runBuild</code> 开始，经过判断是否支持 <code>buildkit</code> ，如果不支持 <code>buildkit</code> 则继续使用 v1 的 <code>builder</code>。接下来读取各类参数，按照不同的参数执行各类不同的处理逻辑。这里需要注意的就是 <code>Dockerfile</code> 及 <code>build context</code> 都可支持从文件或者 <code>stdin</code> 等读入，具体使用时，需要注意。</p>
<p>另外 <code>.dockerignore</code> 文件可过滤掉 <code>build context</code> 中的一些文件，在使用时，可通过此方法进行构建效率的优化，当然也需要注意，在通过 URL 获取 <code>Dockerfile</code> 的时候，是不存在 <code>build context</code> 的，所以类似 <code>COPY</code> 这样的命令也就无法使用了。</p>
<p>当所有的 <code>build context</code> 和参数都准备就绪后，接下来调用封装好的客户端，将这些请求按照本文开始之初介绍的 API 发送给 <code>dockerd</code> ，由其进行真正的构建逻辑。</p>
<p>最后当构建结束后，CLI 根据参数决定是否要显示构建进度或者结果。</p>
<h3>buildkit</h3>
<p>接下来我们来看看 <code>buildkit</code> 如何来执行构建，方法入口与 <code>builder</code> 一致，但是在 <code>buildkitEnabled</code> 处，由于开启了 <code>buildkit</code> 支持，所以跳转到了 <code>runBuildBuildKit</code>。</p>
<pre><code class="language-go">func runBuild(dockerCli command.Cli, options buildOptions) error {
    buildkitEnabled, err := command.BuildKitEnabled(dockerCli.ServerInfo())
    if err != nil {
        return err
    }
    if buildkitEnabled {
        return runBuildBuildKit(dockerCli, options)
    }
    // 省略掉了对于 builder 的实际逻辑
}
</code></pre>
<h4>创建会话</h4>
<p>但是与 <code>builder</code> 不同的是，这里先执行了一次 <code>trySession</code> 函数。</p>
<pre><code class="language-go">// cli/command/image/build_buildkit.go#L48
s, err := trySession(dockerCli, options.context, false)
if err != nil {
    return err
}
if s == nil {
    return errors.Errorf(&quot;buildkit not supported by daemon&quot;)
}
</code></pre>
<p>这个函数是用来做什么的呢？我们来找到该函数所在的文件 <code>cli/command/image/build_session.go</code></p>
<pre><code class="language-go">// cli/command/image/build_session.go#L37
func trySession(dockerCli command.Cli, contextDir string, forStream bool) (*session.Session, error) {
    var s *session.Session
    if isSessionSupported(dockerCli, forStream) {
        sharedKey, err := getBuildSharedKey(contextDir)
        if err != nil {
            return nil, errors.Wrap(err, &quot;failed to get build shared key&quot;)
        }
        s, err = session.NewSession(context.Background(), filepath.Base(contextDir), sharedKey)
        if err != nil {
            return nil, errors.Wrap(err, &quot;failed to create session&quot;)
        }
    }
    return s, nil
}
</code></pre>
<p>当然还包括它其中最主要的 <code>isSessionSupported</code> 函数：</p>
<pre><code class="language-go">// cli/command/image/build_session.go#L30
func isSessionSupported(dockerCli command.Cli, forStream bool) bool {
    if !forStream &amp;&amp; versions.GreaterThanOrEqualTo(dockerCli.Client().ClientVersion(), &quot;1.39&quot;) {
        return true
    }
    return dockerCli.ServerInfo().HasExperimental &amp;&amp; versions.GreaterThanOrEqualTo(dockerCli.Client().ClientVersion(), &quot;1.31&quot;)
}
</code></pre>
<p><code>isSessionSupported</code> 很明显是用于判断是否支持 <code>Session</code>，这里由于我们会传入 <code>forStream</code> 为 <code>false</code> ，而且当前的 API 版本是 1.40 比 1.39 大，所以此函数会返回 <code>true</code> 。其实在 <code>builder</code> 中也执行过相同的逻辑，只不过是在传递了 <code>--stream</code> 参数后，使用 <code>Session</code> 获取一个长连接以达到 <code>stream</code> 的处理能力。</p>
<p>这也就是为什么会有下面 <code>dockerCli.ServerInfo().HasExperimental &amp;&amp; versions.GreaterThanOrEqualTo(dockerCli.Client().ClientVersion(), &quot;1.31&quot;)</code> 这个判断存在的原因了。</p>
<p>当确认支持 <code>Session</code> 时，则会调用 <code>session.NewSession</code> 创建一个新的会话。</p>
<pre><code class="language-go">// github.com/moby/buildkit/session/session.go#L45
func NewSession(ctx context.Context, name, sharedKey string) (*Session, error) {
    id := identity.NewID()

    serverOpts := []grpc.ServerOption{}
    if span := opentracing.SpanFromContext(ctx); span != nil {
        tracer := span.Tracer()
        serverOpts = []grpc.ServerOption{
            grpc.StreamInterceptor(otgrpc.OpenTracingStreamServerInterceptor(span.Tracer(), traceFilter())),
            grpc.UnaryInterceptor(otgrpc.OpenTracingServerInterceptor(tracer, traceFilter())),
        }
    }

    s := &amp;Session{
        id:         id,
        name:       name,
        sharedKey:  sharedKey,
        grpcServer: grpc.NewServer(serverOpts...),
    }

    grpc_health_v1.RegisterHealthServer(s.grpcServer, health.NewServer())

    return s, nil
}
</code></pre>
<p>它创建了一个长连接会话，接下来的操作也都会基于这个会话来做。</p>
<p>接下来的操作与 <code>builder</code> 大体一致，先判断 <code>context</code> 是以哪种形式提供的；当然它也与 <code>builder</code> 一样，是不允许同时从 <code>stdin</code> 获取 <code>Dockerfile</code> 和 <code>build context</code> 。</p>
<pre><code class="language-go">switch {
case options.contextFromStdin():
    // 省略处理逻辑
case isLocalDir(options.context):
    // 省略处理逻辑
case urlutil.IsGitURL(options.context):
    // 省略处理逻辑
case urlutil.IsURL(options.context):
    // 省略处理逻辑
default:
    return errors.Errorf(&quot;unable to prepare context: path %q not found&quot;, options.context)
}
</code></pre>
<p>这里的处理逻辑与 v1 <code>builder</code> 保持一致的原因，主要在于用户体验上，当前的 CLI 的功能已经基本稳定，用户也已经习惯，所以即使是增加了 <code>buildkit</code> 也并没有对主体的操作逻辑造成多大改变。</p>
<h4>选择输出模式</h4>
<p><code>buildkit</code> 支持了三种不同的输出模式 <code>local</code> <code>tar</code> 和正常模式（即存储在 <code>dockerd</code> 中）， 格式为 <code>-o type=local,dest=path</code> 如果需要将构建的镜像进行分发，或是需要进行镜像内文件浏览的话，使用这个方式也是很方便的。</p>
<pre><code class="language-go">outputs, err := parseOutputs(options.outputs)
if err != nil {
    return errors.Wrapf(err, &quot;failed to parse outputs&quot;)
}

for _, out := range outputs {
    switch out.Type {
    case &quot;local&quot;:
        // 省略
    case &quot;tar&quot;:
        // 省略
    }
}
</code></pre>
<p><strong>其实它支持的模式还有第 4 种， 名为 cacheonly 但它并不会像前面提到的三种模式一样，有个很直观的输出，而且用的人可能会很少，所以就没有单独写了。</strong></p>
<h4>读取认证信息</h4>
<pre><code class="language-go">s.Allow(authprovider.NewDockerAuthProvider(os.Stderr))
</code></pre>
<p>这里的行为与上面提到的 <code>builder</code> 的行为基本一致，这里主要有两个需要注意的点：</p>
<ul>
<li>Allow() 函数</li>
</ul>
<pre><code class="language-go">func (s *Session) Allow(a Attachable) {
    a.Register(s.grpcServer)
}
</code></pre>
<p>这个 <code>Allow</code> 函数就是允许通过上面提到的 grpc 会话访问给定的服务。</p>
<ul>
<li><code>authprovider</code></li>
</ul>
<p><code>authprovider</code> 是 <code>buildkit</code> 提供的一组抽象接口集合，通过它们可以访问到机器上的配置文件，进而拿到认证信息，行为与 <code>builder</code> 基本一致。</p>
<h4>高阶特性：<code>secrets</code> 和 <code>ssh</code></h4>
<p>在前一篇 Chat <a href="https://gitbook.cn/gitchat/activity/5cdc40db94539c0c5ded160c">进阶：Dockerfile 高阶使用指南及镜像优化</a> 我已经讲过这两种高阶特性的使用了，本篇中就不再多使用进行过多说明了，只来大体看下该部分的原理和逻辑。</p>
<p><code>secretsprovider</code> 和 <code>sshprovider</code> 都是 <code>buildkit</code> 在提供的，利用这两种特性可以在 Docker 镜像进行构建时更加安全，且更加灵活。</p>
<pre><code class="language-go">func parseSecretSpecs(sl []string) (session.Attachable, error) {
    fs := make([]secretsprovider.FileSource, 0, len(sl))
    for _, v := range sl {
        s, err := parseSecret(v)
        if err != nil {
            return nil, err
        }
        fs = append(fs, *s)
    }
    store, err := secretsprovider.NewFileStore(fs)
    if err != nil {
        return nil, err
    }
    return secretsprovider.NewSecretProvider(store), nil
}
</code></pre>
<p>关于 <code>secrets</code> 方面，最终的 <code>parseSecret</code> 会完成格式相关的校验之类的；</p>
<pre><code class="language-go">func parseSSHSpecs(sl []string) (session.Attachable, error) {
    configs := make([]sshprovider.AgentConfig, 0, len(sl))
    for _, v := range sl {
        c, err := parseSSH(v)
        if err != nil {
            return nil, err
        }
        configs = append(configs, *c)
    }
    return sshprovider.NewSSHAgentProvider(configs)
}
</code></pre>
<p>而关于 <code>ssh</code> 方面，则与上方的 <code>secrets</code> 基本一致，通过 <code>sshprovider</code> 允许进行 ssh 转发之类的，这里不再深入展开了。</p>
<h4>调用 API 发送构建请求</h4>
<p>这里主要有两种情况。</p>
<ul>
<li>当 <code>build context</code> 是从 <code>stdin</code> 读，并且是一个 <code>tar</code> 文件时</li>
</ul>
<pre><code class="language-go">buildID := stringid.GenerateRandomID()
if body != nil {
    eg.Go(func() error {
        buildOptions := types.ImageBuildOptions{
            Version: types.BuilderBuildKit,
            BuildID: uploadRequestRemote + &quot;:&quot; + buildID,
        }

        response, err := dockerCli.Client().ImageBuild(context.Background(), body, buildOptions)
        if err != nil {
            return err
        }
        defer response.Body.Close()
        return nil
    })
}
</code></pre>
<p>它会执行这部分逻辑，但同时也要注意，这是使用的是 Golang 的 <code>goroutine</code>，到这里也并不是结束，这部分代码之后的代码也同样会被执行。这就说到了另一种情况了(通常情况)。</p>
<ul>
<li>使用 <code>doBuild</code> 完成逻辑</li>
</ul>
<pre><code class="language-go">eg.Go(func() error {
    defer func() {
        s.Close()
    }()

    buildOptions := imageBuildOptions(dockerCli, options)
    buildOptions.Version = types.BuilderBuildKit
    buildOptions.Dockerfile = dockerfileName
    buildOptions.RemoteContext = remote
    buildOptions.SessionID = s.ID()
    buildOptions.BuildID = buildID
    buildOptions.Outputs = outputs
    return doBuild(ctx, eg, dockerCli, stdoutUsed, options, buildOptions)
})
</code></pre>
<p>那 <code>doBuild</code> 会做些什么呢？它同样也调用了 API 向 <code>dockerd</code> 发起了构建请求。</p>
<pre><code class="language-go">func doBuild(ctx context.Context, eg *errgroup.Group, dockerCli command.Cli, stdoutUsed bool, options buildOptions, buildOptions types.ImageBuildOptions) (finalErr error) {
    response, err := dockerCli.Client().ImageBuild(context.Background(), nil, buildOptions)
    if err != nil {
        return err
    }
    // 省略
}
</code></pre>
<p>从以上的介绍我们可以先做个小的总结。 <strong>当 build context 从 stdin 读，并且是个 tar 归档时，实际会向 dockerd 发起两次 /build 请求</strong> 而一般情况下只会发送一次请求。</p>
<p>那这里会有什么差别呢？此处先不展开，我们留到下面讲 <code>dockerd</code> 后端的时候再来解释。</p>
<h4>小结</h4>
<p>这里我们对开启了 <code>buildkit</code> 支持的 CLI 构建镜像的过程进行了分析，大致过程如下：</p>
<p>从入口函数 <code>runBuild</code> 开始，判断是否支持 <code>buildkit</code> ，如果支持 <code>buildkit</code> 则调用 <code>runBuildBuildKit</code>。与 v1 的 <code>builder</code> 不同的是，开启了 <code>buildkit</code> 后，会首先创建一个长连接的会话，并一直保持。</p>
<p>其次，与 <code>builder</code> 相同，判断 <code>build context</code> 的来源，格式之类的，校验参数等。当然，<code>buildkit</code> 支持三种不同的输出格式 <code>tar</code>, <code>local</code> 或正常的存储于 Docker 的目录中。</p>
<p>另外是在 <code>buildkit</code> 中新增的高阶特性，可以配置 <code>secrets</code> 和 <code>ssh</code> 密钥等功能。</p>
<p>最后，再调用 API 与 <code>dockerd</code> 交互完成镜像的构建。</p>
<h3>服务端：dockerd</h3>
<p>上面分别介绍了 API， CLI 的 v1 <code>builder</code> 和 <code>buildkit</code> ，接下来我们看看服务端的具体原理和逻辑。</p>
<h4>Client 函数</h4>
<p>还记得上面部分中最后通过 API 与服务端交互的 <code>ImageBuild</code> 函数吗？在开始 <code>dockerd</code> 的介绍前，我们来看下这个客户端接口的具体内容。</p>
<pre><code class="language-go">// github.com/docker/docker/client/image_build.go#L21
func (cli *Client) ImageBuild(ctx context.Context, buildContext io.Reader, options types.ImageBuildOptions) (types.ImageBuildResponse, error) {
    query, err := cli.imageBuildOptionsToQuery(options)
    if err != nil {
        return types.ImageBuildResponse{}, err
    }

    headers := http.Header(make(map[string][]string))
    buf, err := json.Marshal(options.AuthConfigs)
    if err != nil {
        return types.ImageBuildResponse{}, err
    }
    headers.Add(&quot;X-Registry-Config&quot;, base64.URLEncoding.EncodeToString(buf))

    headers.Set(&quot;Content-Type&quot;, &quot;application/x-tar&quot;)

    serverResp, err := cli.postRaw(ctx, &quot;/build&quot;, query, buildContext, headers)
    if err != nil {
        return types.ImageBuildResponse{}, err
    }

    osType := getDockerOS(serverResp.header.Get(&quot;Server&quot;))

    return types.ImageBuildResponse{
        Body:   serverResp.body,
        OSType: osType,
    }, nil
}
</code></pre>
<p>没有什么太特别的地方，行为与 API 一致。 通过这里我们确认它确实访问的 <code>/build</code> 接口，所以，我们来看看 <code>dockerd</code> 的 <code>/build</code> 接口，看看它在构建镜像的时候做了什么。</p>
<h4><code>dockerd</code></h4>
<p>由于本次 Chat 集中讨论的是构建系统相关的部分，所以也就不再过多赘述与构建无关的内容了，我们直接来看，当 CLI 通过 <code>/build</code> 接口发送请求后，会发生什么。</p>
<p>先来看该 API 的入口：</p>
<pre><code class="language-go">// api/server/router/build/build.go#L32
func (r *buildRouter) initRoutes() {
    r.routes = []router.Route{
        router.NewPostRoute(&quot;/build&quot;, r.postBuild),
        router.NewPostRoute(&quot;/build/prune&quot;, r.postPrune),
        router.NewPostRoute(&quot;/build/cancel&quot;, r.postCancel),
    }
}
</code></pre>
<p><code>dockerd</code> 提供了一套类 RESTful 的后端接口服务，处理逻辑的入口便是上面的 <code>postBuild</code> 函数。</p>
<p>该函数的内容较多，我们来分解下它的主要步骤。</p>
<pre><code class="language-go">buildOptions, err := newImageBuildOptions(ctx, r)
if err != nil {
    return errf(err)
}
</code></pre>
<p><strong>newImageBuildOptions 函数就是构造构建参数的，将通过 API 提交过来的参数转换为构建动作实际需要的参数形式。</strong></p>
<pre><code class="language-go">buildOptions.AuthConfigs = getAuthConfigs(r.Header)
</code></pre>
<p><strong>getAuthConfigs 函数用于从请求头拿到认证信息</strong></p>
<pre><code class="language-go">imgID, err := br.backend.Build(ctx, backend.BuildConfig{
    Source:         body,
    Options:        buildOptions,
    ProgressWriter: buildProgressWriter(out, wantAux, createProgressReader),
})
if err != nil {
    return errf(err)
}
</code></pre>
<p>这里就需要注意了: 真正的构建过程要开始了。<strong>使用 backend 的 Build 函数来完成真正的构建过程</strong></p>
<pre><code class="language-go">// api/server/backend/build/backend.go#L52
func (b *Backend) Build(ctx context.Context, config backend.BuildConfig) (string, error) {
    options := config.Options
    useBuildKit := options.Version == types.BuilderBuildKit

    tagger, err := NewTagger(b.imageComponent, config.ProgressWriter.StdoutFormatter, options.Tags)
    if err != nil {
        return &quot;&quot;, err
    }

    var build *builder.Result
    if useBuildKit {
        build, err = b.buildkit.Build(ctx, config)
        if err != nil {
            return &quot;&quot;, err
        }
    } else {
        build, err = b.builder.Build(ctx, config)
        if err != nil {
            return &quot;&quot;, err
        }
    }

    if build == nil {
        return &quot;&quot;, nil
    }

    var imageID = build.ImageID
    if options.Squash {
        if imageID, err = squashBuild(build, b.imageComponent); err != nil {
            return &quot;&quot;, err
        }
        if config.ProgressWriter.AuxFormatter != nil {
            if err = config.ProgressWriter.AuxFormatter.Emit(&quot;moby.image.id&quot;, types.BuildResult{ID: imageID}); err != nil {
                return &quot;&quot;, err
            }
        }
    }

    if !useBuildKit {
        stdout := config.ProgressWriter.StdoutFormatter
        fmt.Fprintf(stdout, &quot;Successfully built %s\n&quot;, stringid.TruncateID(imageID))
    }
    if imageID != &quot;&quot; {
        err = tagger.TagImages(image.ID(imageID))
    }
    return imageID, err
}
</code></pre>
<p>这个函数看着比较长，但主要功能就以下三点：</p>
<ul>
<li><code>NewTagger</code> 是用于给镜像打标签，也就是我们的 <code>-t</code> 参数相关的内容，这里不做展开。</li>
<li>通过判断是否使用了 <code>buildkit</code> 来调用不同的构建后端。</li>
</ul>
<pre><code class="language-go">useBuildKit := options.Version == types.BuilderBuildKit

var build *builder.Result
if useBuildKit {
    build, err = b.buildkit.Build(ctx, config)
    if err != nil {
        return &quot;&quot;, err
    }
} else {
    build, err = b.builder.Build(ctx, config)
    if err != nil {
        return &quot;&quot;, err
    }
}
</code></pre>
<ul>
<li>处理构建完成后的动作。</li>
</ul>
<p>到这个函数之后，就分别是 v1 <code>builder</code> 与 <code>buildkit</code> 对 <code>Dockerfile</code> 的解析，以及对 <code>build context</code> 的操作了。</p>
<p>这里涉及到的内容与之前的 Chat <a href="https://gitbook.cn/gitchat/activity/5cd527e864de19331ba79278">高效构建 Docker 镜像的最佳实践</a> 镜像的内部关联比较大，此处就不再进行展开了。</p>
<h3>总结</h3>
<p>本次 Chat 首先介绍了 Docker 的 C/S 架构，介绍了构建镜像所用的 API , API 文档可以在线查看或者本地构建。</p>
<p>之后深入到 Docker CLI 的源码中，逐步分解 v1 <code>builder</code> 与 <code>buildkit</code> 在构建镜像时执行的过程的差异。</p>
<p>最后，我们深入到 <code>dockerd</code> 的源码中，了解到了对不同构建后端的调用。至此，Docker 构建镜像的原理及主体代码就介绍完毕。</p>
<p>但这还并不是结束，下一场 Chat <a href="https://gitbook.cn/gitchat/activity/5d0b4b1066a9e7233095d288">OCI 与下一代镜像构建工具</a> 中，我将与你分享容器镜像的前世今生，OCI 镜像与 Docker 镜像的异同，以及介绍下一代无 Docker 依赖的镜像构建工具，相信通过下一次的 Chat 你会对容器镜像的生态体系有更加深入的理解。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="AQS&#32;万字图文全面解析.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="ElasticSearch&#32;小白从入门到精通.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43624469b3645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
