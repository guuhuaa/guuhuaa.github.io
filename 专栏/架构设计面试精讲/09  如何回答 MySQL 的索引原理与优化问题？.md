<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>09  如何回答 MySQL 的索引原理与优化问题？.md</title>
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

                    <a class="current-tab" href="09&#32;&#32;如何回答&#32;MySQL&#32;的索引原理与优化问题？.md">09  如何回答 MySQL 的索引原理与优化问题？.md</a>
                    

                </li>
                <li>

                    
                    <a href="10&#32;&#32;如何回答&#32;MySQL&#32;的事务隔离级别和锁的机制？.md">10  如何回答 MySQL 的事务隔离级别和锁的机制？.md</a>

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
                        <div><h1>09  如何回答 MySQL 的索引原理与优化问题？</h1>
<p>在互联网技术面试中，面试官除了会考察分布式、中间件等技术以外，还会考察数据库知识。无论你是程序员，还是架构师，都要掌握关系型数据库 MySQL 的原理与设计问题，从今天起，我就用 4 讲的时间带你打卡 MySQL 的面试内容。</p>
<p>今天这一讲，我们就先来看一看怎么回答 MySQL 的索引原理与优化问题。</p>
<h3>案例背景</h3>
<p>很多面试官考察候选人对“数据库知识”的掌握程度，会以“数据库的索引原理和优化方法”作为切入点。</p>
<p><strong>假设面试官问你：</strong> 在电商平台的订单中心系统中，通常要根据商品类型、订单状态筛选出需要的订单，并按照订单创建的时间进行排序，<strong>那针对下面这条 SQL，你怎么通过索引来提高查询效率呢？</strong></p>
<pre><code>select * from order where status = 1 order by create_time asc
</code></pre>
<p>有的同学会认为，单独给 status 建立一个索引就可以了。</p>
<p>但是更优的方式是建立一个 status 和 create_time 组合索引，这是为了避免 MySQL 数据库发生文件排序。因为在查询时，你只能用到 status 的索引，但如果要对 create_time 排序，就要用文件排序 filesort，也就是在 SQL 执行计划中，Extra 列会出现 Using filesort。</p>
<p>所以你要利用索引的有序性，在 status 和 create_time 列建立联合索引，这样根据 status 筛选后的数据就是按照 create_time 排好序的，避免在文件排序。</p>
<h3>案例分析</h3>
<p>通过这个案例，你可以发现“索引知识”的重要性，所以我一般也会拿索引知识来考察候选人，并扩展出 MySQL 索引原理与优化策略的一系列问题，比如：</p>
<ul>
<li>数据库索引底层使用的是什么数据结构和算法呢？</li>
<li>为什么 MySQL InnoDB 选择 B+Tree 当默认的索引数据结构？</li>
<li>如何通过执行计划查看索引使用详情？</li>
<li>有哪些情况会导致索引失效？</li>
<li>平时有哪些常见的优化索引的方法？</li>
<li>……</li>
</ul>
<p>总结起来就是如下几点：</p>
<ul>
<li>理解 MySQL InnoDB 的索引原理；</li>
<li>掌握 B+Tree 相比于其他索引数据结构（如 B-Tree、二叉树，以及 Hash 表）的优势；</li>
<li>掌握 MySQL 执行计划的方法；</li>
<li>掌握导致索引失效的常见情况；</li>
<li>掌握实际工作中常用的建立高效索引的技巧（如前缀索引、建立覆盖索引等）。</li>
</ul>
<p>如果你曾经被问到其中某一个问题，那你就有必要认真夯实 MySQL 索引及优化的内容了。</p>
<h3>案例解答</h3>
<h4>MySQL InnoDB 的索引原理</h4>
<p><strong>从数据结构的角度来看，</strong> MySQL 常见索引有 B+Tree 索引、HASH 索引、Full-Text 索引。我在表中总结了 MySQL 常见的存储引擎 InnoDB、MyISAM 和 Memory 分别支持的索引类型。（后两个存储引擎在实际工作和面试中很少提及，所以本讲我只讲 InnoDB） 。</p>
<p><img src="assets/Ciqc1GARAb2AeSnCAAF73_MTZck998.png" alt="1.png" /></p>
<p>索引类型</p>
<p>在实际应用中，InnoDB 是 MySQL 建表时默认的存储引擎，B+Tree 索引类型也是 MySQL 存储引擎采用最多的索引类型。</p>
<p>在创建表时，InnoDB 存储引擎默认使用表的主键作为主键索引，该主键索引就是聚簇索引（Clustered Index），如果表没有定义主键，InnoDB 就自己产生一个隐藏的 6 个字节的主键 ID 值作为主键索引，而创建的主键索引默认使用的是 B+Tree 索引。</p>
<p>接下来我们通过一个简单的例子，说明一下 B+Tree 索引在存储数据中的具体实现，<strong>为的是让你理解通过 B+Tree 做索引的原理。</strong></p>
<p>首先，我们创建一张商品表：</p>
<pre><code>CREATE TABLE `product`  (

  `id` int(11) NOT NULL,

  `product_no` varchar(20)  DEFAULT NULL,

  `name` varchar(255) DEFAULT NULL,

  `price` decimal(10, 2) DEFAULT NULL,

  PRIMARY KEY (`id`) USING BTREE

) CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
</code></pre>
<p>然后新增几行数据：
<img src="assets/Cip5yGARAfSAAeR4AAJlafpM_D0118.png" alt="2.png" /></p>
<p>商品数据表</p>
<ul>
<li><strong>通过主键查询（主键索引）商品数据的过程</strong></li>
</ul>
<p>此时当我们使用主键索引查询商品 15 的时候，那么按照 B+Tree 索引原理，是如何找到对应数据的呢？</p>
<pre><code>select * from product where id = 15
</code></pre>
<p>我们可以通过数据手动构建一个 B+Tree，它的每个节点包含 3 个子节点（B+Tree 每个节点允许有 M 个子节点，且 M&gt;2），根节点中的数据值 1、18、36 分别是子节点（1，6，12），（18，24，30）和（36，41，52）中的最小值。</p>
<p>每一层父节点的数据值都会出现在下层子节点的数据值中，因此在叶子节点中，包括了所有的数据值信息，并且每一个叶子节点都指向下一个叶子节点，形成一个链表。如图所示：</p>
<p><img src="assets/CgpVE2ARAp2AKn1rAAuwHY1j7B4280.png" alt="3.png" /></p>
<p>主键索引查询过程</p>
<p>我们举例讲解一下 B+Tree 的查询流程，比如想要查找数据值 15，B+Tree 会自顶向下逐层进行查找：</p>
<ul>
<li>将 15 与根节点的数据 (1，18，36) 比较，15 在 1 和 18 之间，所以根据 B+Tree的搜索逻辑，找到第二层的数据块 (1，6，12)；</li>
<li>在第二层的数据块 (1，6，12) 中进行查找，因为 15 大于 12，所以找到第三层的数据块 (12，15，17)；</li>
<li>在叶子节点的数据块 (12，15，17) 中进行查找，然后我们找到了数据值 15；</li>
<li>最终根据数据值 15 找到叶子节点中存储的数据。</li>
</ul>
<p><strong>整个过程一共进行了 3 次 I/O 操作，所以 B+Tree 相比于 B 树和二叉树来说，最大的优势在于查询效率。</strong></p>
<p>那么问题来了，如果你当前查询数据时候，不是通过主键 ID，而是用商品编码查询商品，那么查询过程又是怎样的呢？</p>
<ul>
<li><strong>通过非主键（辅助索引）查询商品数据的过程</strong></li>
</ul>
<p>如果你用商品编码查询商品（即使用辅助索引进行查询），会先检索辅助索引中的 B+Tree 的 商品编码，找到对应的叶子节点，获取主键值，然后再通过主键索引中的 B+Tree 树查询到对应的叶子节点，然后获取整行数据。<strong>这个过程叫回表。</strong></p>
<p><strong>以上就是索引的实现原理。</strong> 掌握索引的原理是了解 MySQL 数据库的查询效率的基础，是每一个研发工程师都需要精通的知识点。</p>
<p>在面试时，面试官一般不会让你直接描述查询索引的过程，但是会通过考察你对索引优化方法的理解，来评估你对索引原理的掌握程度，比如为什么 MySQL InnoDB 选择 B+Tree 作为默认的索引数据结构？MySQL 常见的优化索引的方法有哪些？</p>
<p>所以接下来，我们就详细了解一下在面试中如何回答索引优化的问题。</p>
<h4>B+Tree 索引的优势</h4>
<p>如果你被问到“为什么 MySQL 会选择 B+Tree 当索引数据结构？”其实在考察你两个方面： B+Tree 的索引原理； B+Tree 索引相比于其他索引类型的优势。</p>
<p>我们刚刚已经讲了 B+Tree 的索引原理，现在就来回答一下 B+Tree 相比于其他常见索引结构，如 B 树、二叉树或 Hash 索引结构的优势在哪儿？</p>
<ul>
<li><strong>B+Tree 相对于 B 树 索引结构的优势</strong></li>
</ul>
<p>B+Tree 只在叶子节点存储数据，而 B 树 的非叶子节点也要存储数据，所以 B+Tree 的单个节点的数据量更小，在相同的磁盘 I/O 次数下，就能查询更多的节点。</p>
<p>另外，B+Tree 叶子节点采用的是双链表连接，适合 MySQL 中常见的基于范围的顺序查找，而 B 树无法做到这一点。</p>
<ul>
<li><strong>B+Tree 相对于二叉树索引结构的优势</strong></li>
</ul>
<p>对于有 N 个叶子节点的 B+Tree，其搜索复杂度为O(logdN)，其中 d 表示节点允许的最大子节点个数为 d 个。在实际的应用当中， d 值是大于100的，这样就保证了，即使数据达到千万级别时，B+Tree 的高度依然维持在 3~4 层左右，也就是说一次数据查询操作只需要做 3~4 次的磁盘 I/O 操作就能查询到目标数据（这里的查询参考上面 B+Tree 的聚簇索引的查询过程）。</p>
<p>而二叉树的每个父节点的儿子节点个数只能是 2 个，意味着其搜索复杂度为 O(logN)，这已经比 B+Tree 高出不少，因此二叉树检索到目标数据所经历的磁盘 I/O 次数要更多。</p>
<ul>
<li><strong>B+Tree 相对于 Hash 表存储结构的优势</strong></li>
</ul>
<p>我们知道范围查询是 MySQL 中常见的场景，但是 Hash 表不适合做范围查询，它更适合做等值的查询，这也是 B+Tree 索引要比 Hash 表索引有着更广泛的适用场景的原因。</p>
<p>至此，你就知道“为什么 MySQL 会选择 B+Tree 来做索引”了。在回答时，你要着眼于 B+Tree 的优势，然后再引入索引原理的查询过程（掌握这些知识点，这个问题其实比较容易回答）。</p>
<p>接下来，我们进入下一个问题：在实际工作中如何查看索引的执行计划。</p>
<h4>通过执行计划查看索引使用详情</h4>
<p>我这里有一张存储商品信息的演示表 product：</p>
<pre><code>CREATE TABLE `product`  (

  `id` int(11) NOT NULL,

  `product_no` varchar(20)  DEFAULT NULL,

  `name` varchar(255) DEFAULT NULL,

  `price` decimal(10, 2) DEFAULT NULL,

  PRIMARY KEY (`id`) USING BTREE,

  KEY 'index_name' ('name').

  KEY 'index_id_name' ('id', 'name')

) CHARACTER SET = utf8 COLLATE = utf8_general_ci
</code></pre>
<p>表中包含了主键索引、name 字段上的普通索引，以及 id 和 name 两个字段的联合索引。现在我们来看一条简单查询语句的执行计划：</p>
<p><img src="assets/CgqCHmARAz-AEslxAAFQoCZRpY4822.png" alt="4.png" /></p>
<p>执行计划</p>
<p>对于执行计划，参数有 possible_keys 字段表示可能用到的索引，key 字段表示实际用的索引，key_len 表示索引的长度，rows 表示扫描的数据行数。</p>
<p><strong>这其中需要你重点关注 type 字段，</strong> 表示数据扫描类型，也就是描述了找到所需数据时使用的扫描方式是什么，常见扫描类型的执行效率从低到高的顺序为（考虑到查询效率问题，全表扫描和全索引扫描要尽量避免）：</p>
<ul>
<li>ALL（全表扫描）；</li>
<li>index（全索引扫描）；</li>
<li>range（索引范围扫描）；</li>
<li>ref（非唯一索引扫描）；</li>
<li>eq_ref（唯一索引扫描）；</li>
<li>const（结果只有一条的主键或唯一索引扫描）。</li>
</ul>
<p>总的来说，执行计划是研发工程师分析索引详情必会的技能（很多大厂公司招聘 JD 上写着“SQL 语句调优” ），所以你在面试时也要知道执行计划核心参数的含义，如 type。在回答时，也要以重点参数为切入点，再扩展到其他参数，然后再说自己是怎么做 SQL 优化工作的。</p>
<h4>索引失效的常见情况</h4>
<p>在工作中，我们经常会碰到 SQL 语句不适用已有索引的情况，来看一个索引失效的例子：</p>
<p><img src="assets/CgqCHmARBA-AQThqAAE5tk3towI139.png" alt="5.png" /></p>
<p>这条带有 like 查询的 SQL 语句，没有用到 product 表中的 index_name 索引。</p>
<p><strong>我们结合普通索引的 B+Tree 结构看一下索引失效的原因：</strong> 当 MySQL 优化器根据 name like ‘%路由器’ 这个条件，到索引 index_name 的 B+Tree 结构上进行查询评估时，发现当前节点的左右子节点上的值都有可能符合 '%路由器' 这个条件，于是优化器判定当前索引需要扫描整个索引，并且还要回表查询，不如直接全表扫描。</p>
<p>当然，还有其他类似的索引失效的情况：</p>
<ul>
<li>索引列上做了计算、函数、类型转换操作，这些情况下索引失效是因为查询过程需要扫描整个索引并回表，代价高于直接全表扫描；</li>
<li>like 匹配使用了前缀匹配符 '%abc'；</li>
<li>字符串不加引号导致类型转换；</li>
</ul>
<p><strong>我给你的建议是，</strong> 如果 MySQL 查询优化器预估走索引的代价比全表扫描的代价还要大，则不走对应的索引，直接全表扫描，如果走索引比全表扫描代价小，则使用索引。</p>
<h4>常见优化索引的方法</h4>
<ul>
<li><strong>前缀索引优化</strong></li>
</ul>
<p>前缀索引就是用某个字段中，字符串的前几个字符建立索引，比如我们可以在订单表上对商品名称字段的前 5 个字符建立索引。使用前缀索引是为了减小索引字段大小，可以增加一个索引页中存储的索引值，有效提高索引的查询速度。在一些大字符串的字段作为索引时，使用前缀索引可以帮助我们减小索引项的大小。</p>
<p>但是，前缀索引有一定的局限性，例如 order by 就无法使用前缀索引，无法把前缀索引用作覆盖索引。</p>
<ul>
<li><strong>覆盖索引优化</strong></li>
</ul>
<p>覆盖索引是指 SQL 中 query 的所有字段，在索引 B+tree 的叶子节点上都能找得到的那些索引，从辅助索引中查询得到记录，而不需要通过聚簇索引查询获得。假设我们只需要查询商品的名称、价格，有什么方式可以避免回表呢？</p>
<p>我们可以建立一个组合索引，即商品ID、名称、价格作为一个组合索引。如果索引中存在这些数据，查询将不会再次检索主键索引，从而避免回表。所以，使用覆盖索引的好处很明显，即不需要查询出包含整行记录的所有信息，也就减少了大量的 I/O 操作。</p>
<ul>
<li><strong>联合索引</strong></li>
</ul>
<p>联合索引时，存在<strong>最左匹配原则</strong>，也就是按照最左优先的方式进行索引的匹配。比如联合索引 (userpin, username)，如果查询条件是 WHERE userpin=1 AND username=2，就可以匹配上联合索引；或者查询条件是 WHERE userpin=1，也能匹配上联合索引，但是如果查询条件是 WHERE username=2，就无法匹配上联合索引。</p>
<p>另外，建立联合索引时的字段顺序，对索引效率也有很大影响。越靠前的字段被用于索引过滤的概率越高，实际开发工作中建立联合索引时，要把区分度大的字段排在前面，这样区分度大的字段越有可能被更多的 SQL 使用到。</p>
<p><img src="assets/Ciqc1GARBC6AOagLAACKmpN6OcM499.png" alt="6.png" /></p>
<p>区分度就是某个字段 column 不同值的个数除以表的总行数，比如性别的区分度就很小，不适合建立索引或不适合排在联合索引列的靠前的位置，而 uuid 这类字段就比较适合做索引或排在联合索引列的靠前的位置。</p>
<h3>总结</h3>
<p>今天，我们讲了 MySQL 的索引原理，介绍了 InnoDB 为什么会采用 B+Tree 结构。因为 B+Tree 能够减少单次查询的磁盘访问次数，做到查询效率最大化。另外，我们还讲了如何查看 SQL 的执行计划，从而找到索引失效的问题，并有针对性的做索引优化。</p>
<p>最后，我总结一些你容易在面试中被问到的，索引的使用原则：</p>
<p><img src="assets/CgpVE2ASL8GAcyLgAAKaTC7eoBA481.png" alt="7修改.png" /></p>
<p>另外，你在了解索引优势的同时，也要了解索引存在的问题：索引会带来数据的写入延迟，引入额外的空间消耗；在海量数据下，想要通过索引提升查询效率也是有限的。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="08&#32;案例串联&#32;&#32;如何让系统抗住双十一的预约抢购活动？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="10&#32;&#32;如何回答&#32;MySQL&#32;的事务隔离级别和锁的机制？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435589bdf1645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
