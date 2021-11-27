<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 Redis 事务深入解析.md</title>
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

                    
                    <a href="01&#32;Redis&#32;是如何执行的.md">01 Redis 是如何执行的.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;Redis&#32;快速搭建与使用.md">02 Redis 快速搭建与使用.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;Redis&#32;持久化——RDB.md">03 Redis 持久化——RDB.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;Redis&#32;持久化——AOF.md">04 Redis 持久化——AOF.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Redis&#32;持久化——混合持久化.md">05 Redis 持久化——混合持久化.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;字符串使用与内部实现原理.md">06 字符串使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;附录：更多字符串操作命令.md">07 附录：更多字符串操作命令.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;字典使用与内部实现原理.md">08 字典使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;附录：更多字典操作命令.md">09 附录：更多字典操作命令.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;列表使用与内部实现原理.md">10 列表使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;附录：更多列表操作命令.md">11 附录：更多列表操作命令.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;集合使用与内部实现原理.md">12 集合使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;附录：更多集合操作命令.md">13 附录：更多集合操作命令.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;有序集合使用与内部实现原理.md">14 有序集合使用与内部实现原理.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;附录：更多有序集合操作命令.md">15 附录：更多有序集合操作命令.md</a>

                </li>
                <li>

                    <a class="current-tab" href="16&#32;Redis&#32;事务深入解析.md">16 Redis 事务深入解析.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;Redis&#32;键值过期操作.md">17 Redis 键值过期操作.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;Redis&#32;过期策略与源码分析.md">18 Redis 过期策略与源码分析.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Redis&#32;管道技术——Pipeline.md">19 Redis 管道技术——Pipeline.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;查询附近的人——GEO.md">20 查询附近的人——GEO.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;游标迭代器（过滤器）——Scan.md">21 游标迭代器（过滤器）——Scan.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;优秀的基数统计算法——HyperLogLog.md">22 优秀的基数统计算法——HyperLogLog.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;内存淘汰机制与算法.md">23 内存淘汰机制与算法.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;消息队列——发布订阅模式.md">24 消息队列——发布订阅模式.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;消息队列的其他实现方式.md">25 消息队列的其他实现方式.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;消息队列终极解决方案——Stream（上）.md">26 消息队列终极解决方案——Stream（上）.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;消息队列终极解决方案——Stream（下）.md">27 消息队列终极解决方案——Stream（下）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;实战：分布式锁详解与代码.md">28 实战：分布式锁详解与代码.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;实战：布隆过滤器安装与使用及原理分析.md">29 实战：布隆过滤器安装与使用及原理分析.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;完整案例：实现延迟队列的两种方法.md">30 完整案例：实现延迟队列的两种方法.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;实战：定时任务案例.md">31 实战：定时任务案例.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;实战：RediSearch&#32;高性能的全文搜索引擎.md">32 实战：RediSearch 高性能的全文搜索引擎.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;实战：Redis&#32;性能测试.md">33 实战：Redis 性能测试.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;实战：Redis&#32;慢查询.md">34 实战：Redis 慢查询.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;实战：Redis&#32;性能优化方案.md">35 实战：Redis 性能优化方案.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;实战：Redis&#32;主从同步.md">36 实战：Redis 主从同步.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;实战：Redis哨兵模式（上）.md">37 实战：Redis哨兵模式（上）.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;实战：Redis&#32;哨兵模式（下）.md">38 实战：Redis 哨兵模式（下）.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;实战：Redis&#32;集群模式（上）.md">39 实战：Redis 集群模式（上）.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;实战：Redis&#32;集群模式（下）.md">40 实战：Redis 集群模式（下）.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;案例：Redis&#32;问题汇总和相关解决方案.md">41 案例：Redis 问题汇总和相关解决方案.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;技能学习指南.md">42 技能学习指南.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;加餐：Redis&#32;的可视化管理工具.md">43 加餐：Redis 的可视化管理工具.md</a>

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
                        <div><h1>16 Redis 事务深入解析</h1>
<blockquote>
<p>作为关系型数据库中一项非常重要的基础功能——事务，在 Redis 中是如何处理并使用的？</p>
</blockquote>
<h3>前言</h3>
<p>事务指的是提供一种将多个命令打包，一次性按顺序地执行的机制，并且保证服务器只有在执行完事务中的所有命令后，才会继续处理此客户端的其他命令。</p>
<p>事务也是其他关系型数据库所必备的基础功能，以支付的场景为例，正常情况下只有正常消费完成之后，才会减去账户余额。但如果没有事务的保障，可能会发生消费失败了，但依旧会把账户的余额给扣减了，我想这种情况应该任何人都无法接受吧？所以事务是数据库中一项非常重要的基础功能。</p>
<h3>事务基本使用</h3>
<p>事务在其他语言中，一般分为以下三个阶段：</p>
<ul>
<li>开启事务——Begin Transaction</li>
<li>执行业务代码，提交事务——Commit Transaction</li>
<li>业务处理中出现异常，回滚事务——Rollback Transaction</li>
</ul>
<p>以 Java 中的事务执行为例：</p>
<pre><code class="language-java">// 开启事务
begin();
try {
    //......
    // 提交事务
    commit();
} catch(Exception e) {
    // 回滚事务
    rollback();
}

</code></pre>
<p>Redis 中的事务从开始到结束也是要经历三个阶段：</p>
<ul>
<li>开启事务</li>
<li>命令入列</li>
<li>执行事务/放弃事务</li>
</ul>
<p>其中，开启事务使用 multi 命令，事务执行使用 exec 命令，放弃事务使用 discard 命令。</p>
<h4><strong>开启事务</strong></h4>
<p>multi 命令用于开启事务，实现代码如下：</p>
<pre><code class="language-shell">&gt; multi
OK

</code></pre>
<p>multi 命令可以让客户端从非事务模式状态，变为事务模式状态，如下图所示：</p>
<p><img src="assets/f2898390-5ddf-11ea-9d6d-67bd1a14f4fe" alt="img" /></p>
<p><strong>注意</strong>：multi 命令不能嵌套使用，如果已经开启了事务的情况下，再执行 multi 命令，会提示如下错误：</p>
<pre><code>(error) ERR MULTI calls can not be nested

</code></pre>
<p>执行效果，如下代码所示：</p>
<pre><code class="language-shell">127.0.0.1:6379&gt; multi
OK
127.0.0.1:6379&gt; multi
(error) ERR MULTI calls can not be nested

</code></pre>
<p>当客户端是非事务状态时，使用 multi 命令，客户端会返回结果 OK，如果客户端已经是事务状态，再执行 multi 命令会 multi 命令不能嵌套的错误，但不会终止客户端为事务的状态，如下图所示：</p>
<p><img src="assets/3aa4ae70-5de0-11ea-9d6d-67bd1a14f4fe" alt="img" /></p>
<h4><strong>命令入列</strong></h4>
<p>客户端进入事务状态之后，执行的所有常规 Redis 操作命令（非触发事务执行或放弃和导致入列异常的命令）会依次入列，命令入列成功后会返回 QUEUED，如下代码所示：</p>
<pre><code class="language-shell">&gt; multi
OK
&gt; set k v
QUEUED
&gt; get k
QUEUED

</code></pre>
<p>执行流程如下图所示：</p>
<p><img src="assets/68d8d640-5de0-11ea-9d6d-67bd1a14f4fe" alt="img" /></p>
<p><strong>注意</strong>：命令会按照先进先出（FIFO）的顺序出入列，也就是说事务会按照命令的入列顺序，从前往后依次执行。</p>
<h4><strong>执行事务/放弃事务</strong></h4>
<p>执行事务的命令是 exec，放弃事务的命令是 discard。</p>
<p>执行事务示例代码如下：</p>
<pre><code class="language-shell">&gt; multi
OK
&gt; set k v2
QUEUED
&gt; exec
1) OK
&gt; get k
&quot;v2&quot;

</code></pre>
<p>放弃事务示例代码如下：</p>
<pre><code class="language-shell">&gt; multi
OK
&gt; set k v3
QUEUED
&gt; discard
OK
&gt; get k
&quot;v2&quot;

</code></pre>
<p>执行流程如下图所示：</p>
<p><img src="assets/e31a4ab0-5de0-11ea-9359-3b811418c7dd" alt="img" /></p>
<h3>事务错误&amp;回滚</h3>
<p>事务执行中的错误分为以下三类：</p>
<ul>
<li>执行时才会出现的错误（简称：执行时错误）；</li>
<li>入列时错误，不会终止整个事务；</li>
<li>入列时错误，会终止整个事务。</li>
</ul>
<h4><strong>执行时错误</strong></h4>
<p>示例代码如下：</p>
<pre><code class="language-shell">&gt; get k
&quot;v&quot;
&gt; multi
OK
&gt; set k v2
QUEUED
&gt; expire k 10s
QUEUED
&gt; exec
1) OK
2) (error) ERR value is not an integer or out of range
&gt; get k
&quot;v2&quot;

</code></pre>
<p>执行命令解释如下图所示：</p>
<p><img src="assets/aa0ca950-5de2-11ea-9e6b-b3dcd9fe8595" alt="img" /></p>
<p>从以上结果可以看出，即使事务队列中某个命令在执行期间发生了错误，事务也会继续执行，直到事务队列中所有命令执行完成。</p>
<h4><strong>入列错误不会导致事务结束</strong></h4>
<p>示例代码如下：</p>
<pre><code class="language-shell">&gt; get k
&quot;v&quot;
&gt; multi
OK
&gt; set k v2
QUEUED
&gt; multi
(error) ERR MULTI calls can not be nested
&gt; exec
1) OK
&gt; get k
&quot;v2&quot;

</code></pre>
<p>执行命令解释如下图所示：</p>
<p><img src="assets/cc4111f0-5de2-11ea-9e6b-b3dcd9fe8595" alt="img" /></p>
<p>可以看出，重复执行 multi 会导致入列错误，但不会终止事务，最终查询的结果是事务执行成功了。除了重复执行 multi 命令，还有在事务状态下执行 watch 也是同样的效果，下文会详细讲解关于 watch 的内容。</p>
<h4><strong>入列错误导致事务结束</strong></h4>
<p>示例代码如下：</p>
<pre><code class="language-shell">&gt; get k
&quot;v2&quot;
&gt; multi
OK
&gt; set k v3
QUEUED
&gt; set k
(error) ERR wrong number of arguments for 'set' command
&gt; exec
(error) EXECABORT Transaction discarded because of previous errors.
&gt; get k
&quot;v2&quot;

</code></pre>
<p>执行命令解释如下图所示：</p>
<p><img src="assets/fd00c6a0-5de2-11ea-9d6f-15d639c92acd" alt="img" /></p>
<h4><strong>为什么不支持事务回滚？</strong></h4>
<p>Redis 官方文档的解释如下：</p>
<blockquote>
<p>If you have a relational databases background, the fact that Redis commands can fail during a transaction, but still Redis will execute the rest of the transaction instead of rolling back, may look odd to you.</p>
<p>However there are good opinions for this behavior:</p>
<ul>
<li>Redis commands can fail only if called with a wrong syntax (and the problem is not detectable during the command queueing), or against keys holding the wrong data type: this means that in practical terms a failing command is the result of a programming errors, and a kind of error that is very likely to be detected during development, and not in production.</li>
<li>Redis is internally simplified and faster because it does not need the ability to roll back.</li>
</ul>
<p>An argument against Redis point of view is that bugs happen, however it should be noted that in general the roll back does not save you from programming errors. For instance if a query increments a key by 2 instead of 1, or increments the wrong key, there is no way for a rollback mechanism to help. Given that no one can save the programmer from his or her errors, and that the kind of errors required for a Redis command to fail are unlikely to enter in production, we selected the simpler and faster approach of not supporting roll backs on errors.</p>
</blockquote>
<p>大概的意思是，作者不支持事务回滚的原因有以下两个：</p>
<ul>
<li>他认为 Redis 事务的执行时，错误通常都是编程错误造成的，这种错误通常只会出现在开发环境中，而很少会在实际的生产环境中出现，所以他认为没有必要为 Redis 开发事务回滚功能；</li>
<li>不支持事务回滚是因为这种复杂的功能和 Redis 追求的简单高效的设计主旨不符合。</li>
</ul>
<p>这里不支持事务回滚，指的是不支持运行时错误的事务回滚。</p>
<h3>监控</h3>
<p>watch 命令用于客户端并发情况下，为事务提供一个乐观锁（CAS，Check And Set），也就是可以用 watch 命令来监控一个或多个变量，如果在事务的过程中，某个<strong>监控项被修改</strong>了，那么<strong>整个事务</strong>就会<strong>终止执行</strong>。</p>
<p>watch 基本语法如下：</p>
<pre><code>watch key [key ...]

</code></pre>
<p><code>watch</code> 示例代码如下：</p>
<pre><code class="language-shell">&gt; watch k
OK
&gt; multi
OK
&gt; set k v2
QUEUED
&gt; exec
(nil)
&gt; get k
&quot;v&quot;

</code></pre>
<p><strong>注意</strong>：以上事务在执行期间，也就是开启事务（multi）之后，执行事务（exec）之前，模拟多客户端并发操作了变量 k 的值，这个时候再去执行事务，才会出现如上结果，exec 执行的结果为 nil。</p>
<p>可以看出，当执行 exec 返回的结果是 nil 时，表示 watch 监控的对象在事务执行的过程中被修改了。从 <code>get k</code> 的结果也可以印证，因为事务中设置的值 <code>set k v2</code> 并未正常执行。</p>
<p>执行流程如下图所示：</p>
<p><img src="assets/191ad650-5de3-11ea-9e57-957b6467a3fc" alt="img" /></p>
<p><strong>注意</strong>： watch 命令只能在客户端开启事务之前执行，在事务中执行 watch 命令会引发错误，但不会造成整个事务失败，如下代码所示：</p>
<pre><code class="language-shell">&gt; multi
OK
&gt; set k v3
QUEUED
&gt; watch k
(error) ERR WATCH inside MULTI is not allowed
&gt; exec
1) OK
&gt; get k
&quot;v3&quot;

</code></pre>
<p>执行命令解释如下图所示：</p>
<p><img src="assets/4097f000-5de3-11ea-9e57-957b6467a3fc" alt="img" /></p>
<p>unwatch 命令用于清除所有之前监控的所有对象（键值对）。</p>
<p>unwatch 示例如下所示：</p>
<pre><code class="language-shell">&gt; set k v
OK
&gt; watch k
OK
&gt; multi
OK
&gt; unwatch
QUEUED
&gt; set k v2
QUEUED
&gt; exec
1) OK
2) OK
&gt; get k
&quot;v2&quot;

</code></pre>
<p>可以看出，即使在事务的执行过程中，k 值被修改了，因为调用了 unwatch 命令，整个事务依然会顺利执行。</p>
<h3>代码实战</h3>
<p>以下是事务在 Java 中的使用，代码如下：</p>
<pre><code class="language-java">import redis.clients.jedis.Jedis;
import redis.clients.jedis.Transaction;

public class TransactionExample {
    public static void main(String[] args) {
        // 创建 Redis 连接
        Jedis jedis = new Jedis(&quot;xxx.xxx.xxx.xxx&quot;, 6379);
        // 设置 Redis 密码
        jedis.auth(&quot;xxx&quot;);
        // 设置键值
        jedis.set(&quot;k&quot;, &quot;v&quot;);
        // 开启监视 watch
        jedis.watch(&quot;k&quot;);
        // 开始事务
        Transaction tx = jedis.multi();
        // 命令入列
        tx.set(&quot;k&quot;, &quot;v2&quot;);
        // 执行事务
        tx.exec();
        System.out.println(jedis.get(&quot;k&quot;));
        jedis.close();
    }
}

</code></pre>
<h3>知识点练习</h3>
<h4><strong>以下两个客户端交替执行的结果是？</strong></h4>
<p>客户端一，执行如下命令：</p>
<pre><code class="language-shell">&gt; set k v
OK
&gt; watch k
OK
&gt; multi
OK
&gt; set k v2
QUEUED

</code></pre>
<p>客户端二，执行如下命令：</p>
<pre><code class="language-shell">&gt; set k v
OK

</code></pre>
<p>客户端一，再执行如下命令：</p>
<pre><code class="language-shell">&gt; exec

</code></pre>
<p>此时 k 的值为多少？</p>
<p>答： k 的值为 v，而非 v2。</p>
<p>题目解析：本题考查的是 watch 命令监控时，即使把原对象的值重新赋值给了原对象，这个时候 watch 命令也会认为监控对象还是被修改了。</p>
<h3>小结</h3>
<p>事务为多个命令提供一次性按顺序执行的机制，与 Redis 事务相关的命令有以下五个：</p>
<ul>
<li>multi：开启事务</li>
<li>exec：执行事务</li>
<li>discard：丢弃事务</li>
<li>watch：为事务提供乐观锁实现</li>
<li>unwatch：取消监控（取消事务中的乐观锁）</li>
</ul>
<p>正常情况下 Redis 事务分为三个阶段：开启事务、命令入列、执行事务。Redis 事务并不支持运行时错误的事务回滚，但在某些入列错误，如 <code>set key</code> 或者是 <code>watch</code> 监控项被修改时，提供整个事务回滚的功能。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;附录：更多有序集合操作命令.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;Redis&#32;键值过期操作.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434a03ecda70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Redis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
