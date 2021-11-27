<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10  如何回答 MySQL 的事务隔离级别和锁的机制？.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词&#32;&#32;中高级研发面试，逃不开架构设计这一环.md">00 开篇词  中高级研发面试，逃不开架构设计这一环.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;研发工程师想提升面试竞争力，该具备这三个技术认知.md">01  研发工程师想提升面试竞争力，该具备这三个技术认知.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;研发工程师如何用架构师视角回答架构设计方案？.md">02  研发工程师如何用架构师视角回答架构设计方案？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;面试官如何考察与&#32;CAP&#32;有关的分布式理论？.md">03  面试官如何考察与 CAP 有关的分布式理论？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;亿级商品存储下，如何深度回答分布式系统的原理性问题？.md">04  亿级商品存储下，如何深度回答分布式系统的原理性问题？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;海量并发场景下，如何回答分布式事务一致性问题？.md">05  海量并发场景下，如何回答分布式事务一致性问题？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;分布式系统中，如何回答锁的实现原理？.md">06  分布式系统中，如何回答锁的实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;RPC：如何在面试中展现出“造轮子”的能力？.md">07  RPC：如何在面试中展现出“造轮子”的能力？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;MQ：如何回答消息队列的丢失、重复与积压问题.md">08  MQ：如何回答消息队列的丢失、重复与积压问题.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;案例串联&#32;&#32;如何让系统抗住双十一的预约抢购活动？.md">08 案例串联  如何让系统抗住双十一的预约抢购活动？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;如何回答&#32;MySQL&#32;的索引原理与优化问题？.md">09  如何回答 MySQL 的索引原理与优化问题？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="10&#32;&#32;如何回答&#32;MySQL&#32;的事务隔离级别和锁的机制？.md">10  如何回答 MySQL 的事务隔离级别和锁的机制？.md</a>
                    

                </li>
                <li>

                    
                    <a href="11&#32;&#32;读多写少：MySQL&#32;如何优化数据查询方案？.md">11  读多写少：MySQL 如何优化数据查询方案？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;写多读少：MySQL&#32;如何优化数据存储方案？.md">12  写多读少：MySQL 如何优化数据存储方案？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;缓存原理：应对面试你要掌握&#32;Redis&#32;哪些原理？.md">13  缓存原理：应对面试你要掌握 Redis 哪些原理？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;缓存策略：面试中如何回答缓存穿透、雪崩等问题？.md">14  缓存策略：面试中如何回答缓存穿透、雪崩等问题？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何向面试官证明你做的系统是高可用的？.md">15  如何向面试官证明你做的系统是高可用的？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;如何从架构师角度回答系统容错、降级等高可用问题？.md">16  如何从架构师角度回答系统容错、降级等高可用问题？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何向面试官证明你做的系统是高性能的？.md">17  如何向面试官证明你做的系统是高性能的？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何从架构师角度回答怎么应对千万级流量的问题？.md">18  如何从架构师角度回答怎么应对千万级流量的问题？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;彩蛋&#32;&#32;互联网架构设计面试，你需要掌握的知识体系.md">19 彩蛋  互联网架构设计面试，你需要掌握的知识体系.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;程序员的道、术、势.md">结束语  程序员的道、术、势.md</a>

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
                        <div><h1>10  如何回答 MySQL 的事务隔离级别和锁的机制？</h1>
<p>上一讲，我讲了 MySQL 的索引原理与优化问题，今天我带你继续学习 MySQL 的事务隔离级别和锁的机制，MySQL 的事务和锁是并发控制最基本的手段，在面试中，它们与 09 讲的索引一样，同样是 MySQL 重要的考察点。</p>
<h3>案例背景</h3>
<p>MySQL 的事务隔离级别（Isolation Level），是指：当多个线程操作数据库时，数据库要负责隔离操作，来保证各个线程在获取数据时的准确性。它分为四个不同的层次，按隔离水平高低排序，<strong>读未提交 &lt; 读已提交 &lt; 可重复度 &lt; 串行化</strong>。</p>
<p><img src="assets/CgpVE2AXOh2AEXQqAACGXaq3WXI045.PNG" alt="幻灯片1.PNG" /></p>
<p>MySQL 隔离级别</p>
<ul>
<li><strong>读未提交（Read uncommitted）</strong>：隔离级别最低、隔离度最弱，脏读、不可重复读、幻读三种现象都可能发生。所以它基本是理论上的存在，实际项目中没有人用，但性能最高。</li>
<li><strong>读已提交（Read committed）</strong>：它保证了事务不出现中间状态的数据，所有数据都是已提交且更新的，解决了脏读的问题。但读已提交级别依旧很低，它允许事务间可并发修改数据，所以不保证再次读取时能得到同样的数据，也就是还会存在不可重复读、幻读的可能。</li>
<li><strong>可重复读（Repeatable reads）</strong>：MySQL InnoDB 引擎的默认隔离级别，保证同一个事务中多次读取数据的一致性，解决脏读和不可重复读，但仍然存在幻读的可能。</li>
<li><strong>可串行化（Serializable）</strong>：选择“可串行化”意味着读取数据时，需要获取共享读锁；更新数据时，需要获取排他写锁；如果 SQL 使用 WHERE 语句，还会获取区间锁。换句话说，事务 A 操作数据库时，事务 B 只能排队等待，因此性能也最低。</li>
</ul>
<p>至于数据库锁，分为悲观锁和乐观锁，“悲观锁”认为数据出现冲突的可能性很大，“乐观锁”认为数据出现冲突的可能性不大。那悲观锁和乐观锁在基于 MySQL 数据库的应用开发中，是如何实现的呢？</p>
<ul>
<li>悲观锁一般利用 SELECT … FOR UPDATE 类似的语句，对数据加锁，避免其他事务意外修改数据。</li>
<li>乐观锁利用 CAS 机制，并不会对数据加锁，而是通过对比数据的时间戳或者版本号，实现版本判断。</li>
</ul>
<h3>案例分析</h3>
<p>如果面试官想深挖候选人对数据库内部机制的掌握程度，切入点一般是 MySQL 的事务和锁机制。接下来，我就从初中级研发工程师的角度出发，从概念到实践，带你掌握“MySQL 事务和锁机制”的高频考点：</p>
<ul>
<li>举例说明什么是脏读、不可重复度和幻读（三者虽然基础，但很多同学容易弄混）？</li>
<li>MySQL 是怎么解决脏读、不可重复读，和幻读问题的？</li>
<li>你怎么理解死锁？</li>
<li>……</li>
</ul>
<h3>案例解答</h3>
<h4>怎么理解脏读、不可重复读和幻读？</h4>
<p><strong>脏读：</strong> 读到了未提交事务的数据。</p>
<p><img src="assets/CgpVE2AXOj6AUNXEAABi4cEeRxY560.PNG" alt="幻灯片2.PNG" /></p>
<p>事务并发时的“脏读”现象</p>
<p>假设有 A 和 B 两个事务，在并发情况下，事务 A 先开始读取商品数据表中的数据，然后再执行更新操作，如果此时事务 A 还没有提交更新操作，但恰好事务 B 开始，然后也需要读取商品数据，此时事务 B 查询得到的是刚才事务 A 更新后的数据。</p>
<p>如果接下来事务 A 触发了回滚，那么事务 B 刚才读到的数据就是过时的数据，这种现象就是脏读。</p>
<p><strong>“脏读”面试关注点：</strong></p>
<ol>
<li>脏读对应的隔离级别是“读未提交”，只有该隔离级别才会出现脏读。</li>
<li>脏读的解决办法是升级事务隔离级别，比如“读已提交”。</li>
</ol>
<p><strong>不可重复读：</strong> 事务 A 先读取一条数据，然后执行逻辑的过程中，事务 B 更新了这条数据，事务 A 再读取时，发现数据不匹配，这个现象就是“不可重复读”。</p>
<p><img src="assets/Cip5yGAXOmGAcCNlAABpFaU7YQ8179.PNG" alt="幻灯片3.PNG" /></p>
<p>事务并发时的“不可重复读”现象</p>
<p><strong>“不可重复读”面试关注点：</strong></p>
<ol>
<li>简单理解是两次读取的数据中间被修改，对应的隔离级别是“读未提交”或“读已提交”。</li>
<li>不可重复读的解决办法就是升级事务隔离级别，比如“可重复度”。</li>
</ol>
<p><strong>幻读：</strong> 在一个事务内，同一条查询语句在不同时间段执行，得到不同的结果集。</p>
<p><img src="assets/Cip5yGAXOnSASsgQAABza2XSHV0638.PNG" alt="幻灯片4.PNG" /></p>
<p>事务并发时的“幻读”现象</p>
<p>事务 A 读了一次商品表，得到最后的 ID 是 3，事务 B 也同样读了一次，得到最后 ID 也是 3。接下来事务 A 先插入了一行，然后读了一下最新的 ID 是 4，刚好是前面 ID 3 加上 1，然后事务 B 也插入了一行，接着读了一下最新的 ID 发现是 5，而不是 3 加 1。</p>
<p>这时，你发现在使用 ID 做判断或做关键数据时，就会出现问题，这种现象就像是让事务 B 产生了幻觉一样，读取到了一个意想不到的数据，所以叫幻读。当然，不仅仅是新增，删除、修改数据也会发生类似的情况。</p>
<p><strong>“幻读”面试关注点：</strong></p>
<ol>
<li>要想解决幻读不能升级事务隔离级别到“可串行化”，那样数据库也失去了并发处理能力。</li>
<li>行锁解决不了幻读，因为即使锁住所有记录，还是阻止不了插入新数据。</li>
<li>解决幻读的办法是锁住记录之间的“间隙”，为此 MySQL InnoDB 引入了新的锁，叫<strong>间隙锁（Gap Lock）</strong>，所以在面试中，你也要掌握间隙锁，以及间隙锁与行锁结合的 next-key lock 锁。</li>
</ol>
<h4>怎么理解死锁</h4>
<p>除了事务隔离级别，很多同学在面试时，经常会被面试官直奔主题地问：“谈谈你对死锁的理解”。要回答这样开放的问题，你就要在脑海中梳理出系统化的回答思路：<strong>死锁是如何产生的，如何避免死锁。</strong></p>
<p>死锁一般发生在多线程（两个或两个以上）执行的过程中。因为争夺资源造成线程之间相互等待，这种情况就产生了死锁。我在 06 讲也提到了死锁，但是并没有讲它产生的原因以及怎么避免，所以接下来我们就来了解这部分内容。</p>
<p><img src="assets/CgpVE2AXOoeAIPuHAABkdI2Blp4721.PNG" alt="幻灯片5.PNG" /></p>
<p>线程死锁</p>
<p>比如你有资源 1 和 2，以及线程 A 和 B，当线程 A 在已经获取到资源 1 的情况下，期望获取线程 B 持有的资源 2。与此同时，线程 B 在已经获取到资源 2 的情况下，期望获取现场 A 持有的资源 1。</p>
<p>那么线程 A 和线程 B 就处理了相互等待的死锁状态，在没有外力干预的情况下，线程 A 和线程 B 就会一直处于相互等待的状态，从而不能处理其他的请求。</p>
<p><strong>死锁产生的四个必要条件</strong>。</p>
<p><img src="assets/CgpVE2AXOpyAODwtAABTGjPzh6k531.PNG" alt="幻灯片6.PNG" /></p>
<p>互斥条件</p>
<p><strong>互斥：</strong> 多个线程不能同时使用一个资源。比如线程 A 已经持有的资源，不能再同时被线程 B 持有。如果线程 B 请求获取线程 A 已经占有的资源，那线程 B 只能等待这个资源被线程 A 释放。</p>
<p><img src="assets/Cip5yGAXOq-AF8jDAABSSEnH3dk920.PNG" alt="幻灯片7.PNG" /></p>
<p>持有并等待</p>
<p><strong>持有并等待：</strong> 当线程 A 已经持有了资源 1，又提出申请资源 2，但是资源 2 已经被线程 C 占用，所以线程 A 就会处于等待状态，但它在等待资源 2 的同时并不会释放自己已经获取的资源 1。</p>
<p><img src="assets/Cip5yGAXOsCAA25rAABO_a-VNXU420.PNG" alt="幻灯片8.PNG" /></p>
<p>不可剥夺条件</p>
<p><strong>不可剥夺：</strong> 线程 A 获取到资源 1 之后，在自己使用完之前不能被其他线程（比如线程 B）抢占使用。如果线程 B 也想使用资源 1，只能在线程 A 使用完后，主动释放后再获取。</p>
<p><img src="assets/CgpVE2AXOtuAdm_UAABSLZeUVA0081.PNG" alt="幻灯片9.PNG" /></p>
<p>循环等待</p>
<p><strong>循环等待：</strong> 发生死锁时，必然会存在一个线程，也就是资源的环形链。比如线程 A 已经获取了资源 1，但同时又请求获取资源 2。线程 B 已经获取了资源 2，但同时又请求获取资源 1，这就会形成一个线程和资源请求等待的环形图。</p>
<p>死锁只有同时满足<strong>互斥</strong>、<strong>持有并等待</strong>、<strong>不可剥夺</strong>、<strong>循环等待</strong>时才会发生。并发场景下一旦死锁，一般没有特别好的方法，很多时候只能重启应用。<strong>因此，最好是规避死锁，那么具体怎么做呢？答案是：至少破坏其中一个条件</strong>（互斥必须满足，你可以从其他三个条件出发）。</p>
<ul>
<li>持有并等待：我们可以一次性申请所有的资源，这样就不存在等待了。</li>
<li>不可剥夺：占用部分资源的线程进一步申请其他资源时，如果申请不到，可以主动释放它占有的资源，这样不可剥夺这个条件就破坏掉了。</li>
<li>循环等待：可以靠按序申请资源来预防，也就是所谓的资源有序分配原则，让资源的申请和使用有线性顺序，申请的时候可以先申请资源序号小的，再申请资源序号大的，这样的线性化操作就自然就不存在循环了。</li>
</ul>
<h3>总结</h3>
<p>我们花了两讲的时间，把 MySQL 数据库面试中的高频问题熟悉了一遍，但是如果从数据库领域应用开发者角度出发，至少还需要掌握以下几部分内容。</p>
<ul>
<li><strong>数据库设计基础</strong>：掌握数据库设计中的基本范式，以及基础概念，例如表、视图、索引、外键、序列号生成器等，掌握数据库的数据类型的使用，清楚业务实体关系与数据库结构的映射。</li>
<li><strong>数据库隔离级别</strong>：掌握 MySQL 四种事务隔离级别的基础知识，并进一步了解 MVCC、Locking 等机制对于处理的进阶问题的解决；还需要了解不同索引类型的使用，甚至是底层数据结构和算法等。</li>
<li><strong>SQL 优化</strong>：掌握基础的 SQL 调优技巧，至少要了解基本思路是怎样的，例如 SQL 怎样写才能更好利用索引、知道如何分析 SQL 执行计划等。</li>
<li><strong>数据库架构设计</strong>：掌握针对高并发等特定场景中的解决方案，如读写分离、分库分表等。</li>
</ul>
<p>当然在准备面试时我并不建议你找一堆书闷头苦读，还是要从实际工作中，从使用数据库出发，并结合实践，完善和深化自己的知识体系，今天的内容就讲到这里，我们下一讲见。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;&#32;如何回答&#32;MySQL&#32;的索引原理与优化问题？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;&#32;读多写少：MySQL&#32;如何优化数据查询方案？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43558e08ca645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%9E%B6%E6%9E%84%E8%AE%BE%E8%AE%A1%E9%9D%A2%E8%AF%95%E7%B2%BE%E8%AE%B2/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
