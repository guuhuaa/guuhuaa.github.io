<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>12 聚合：聚合查询之Pipline聚合详解.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    <a class="current-tab" href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>
                    

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>12 聚合：聚合查询之Pipline聚合详解</h1>
<h2>如何理解pipeline聚合</h2>
<blockquote>
<p>如何理解管道聚合呢？最重要的是要站在设计者角度看这个功能的要实现的目的：让上一步的聚合结果成为下一个聚合的输入，这就是管道。</p>
</blockquote>
<h3>管道机制的常见场景</h3>
<blockquote>
<p>首先回顾下，Tomcat管道机制中向你介绍的常见的管道机制设计中的应用场景。</p>
</blockquote>
<h4>责任链模式</h4>
<p>管道机制在设计模式上属于责任链模式，如果你不理解，请参看如下文章：</p>
<p>责任链模式: 通过责任链模式, 你可以为某个请求创建一个对象链. 每个对象依序检查此请求并对其进行处理或者将它传给链中的下一个对象。</p>
<h4>FilterChain</h4>
<p>在软件开发的常接触的责任链模式是FilterChain，它体现在很多软件设计中：</p>
<ul>
<li><strong>比如Spring Security框架中</strong></li>
</ul>
<p><img src="assets/tomcat-x-pipline-6.jpg" alt="img" /></p>
<ul>
<li><strong>比如HttpServletRequest处理的过滤器中</strong></li>
</ul>
<p>当一个request过来的时候，需要对这个request做一系列的加工，使用责任链模式可以使每个加工组件化，减少耦合。也可以使用在当一个request过来的时候，需要找到合适的加工方式。当一个加工方式不适合这个request的时候，传递到下一个加工方法，该加工方式再尝试对request加工。</p>
<p>网上找了图，这里我们后文将通过Tomcat请求处理向你阐述。</p>
<p><img src="assets/tomcat-x-pipline-5.jpg" alt="img" /></p>
<h3>ElasticSearch设计管道机制</h3>
<p>简单而言：让上一步的聚合结果成为下一个聚合的输入，这就是管道。</p>
<p>接下来，无非就是对不同类型的聚合有接口的支撑，比如：</p>
<p><img src="assets/es-agg-pipeline-1.png" alt="img" /></p>
<blockquote>
<p>第一个维度：管道聚合有很多不同<strong>类型</strong>，每种类型都与其他聚合计算不同的信息，但是可以将这些类型分为两类：</p>
</blockquote>
<ul>
<li><strong>父级</strong> 父级聚合的输出提供了一组管道聚合，它可以计算新的存储桶或新的聚合以添加到现有存储桶中。</li>
<li><strong>兄弟</strong> 同级聚合的输出提供的管道聚合，并且能够计算与该同级聚合处于同一级别的新聚合。</li>
</ul>
<blockquote>
<p>第二个维度：根据<strong>功能设计</strong>的意图</p>
</blockquote>
<p>比如前置聚合可能是Bucket聚合，后置的可能是基于Metric聚合，那么它就可以成为一类管道</p>
<p>进而引出了：<code>xxx bucket</code>(是不是很容易理解了 @pdai)</p>
<ul>
<li>
<p>Bucket聚合 -&gt; Metric聚合</p>
<p>： bucket聚合的结果，成为下一步metric聚合的输入</p>
<ul>
<li>Average bucket</li>
<li>Min bucket</li>
<li>Max bucket</li>
<li>Sum bucket</li>
<li>Stats bucket</li>
<li>Extended stats bucket</li>
</ul>
</li>
</ul>
<p>对构建体系而言，理解上面的已经够了，其它的类型不过是锦上添花而言。</p>
<h2>一些例子</h2>
<blockquote>
<p>这里我们通过几个简单的例子看看即可，具体如果需要使用看看文档即可。@pdai</p>
</blockquote>
<h3>Average bucket 聚合</h3>
<pre><code class="language-bash">POST _search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;sales_per_month&quot;: {
      &quot;date_histogram&quot;: {
        &quot;field&quot;: &quot;date&quot;,
        &quot;calendar_interval&quot;: &quot;month&quot;
      },
      &quot;aggs&quot;: {
        &quot;sales&quot;: {
          &quot;sum&quot;: {
            &quot;field&quot;: &quot;price&quot;
          }
        }
      }
    },
    &quot;avg_monthly_sales&quot;: {
// tag::avg-bucket-agg-syntax[]               
      &quot;avg_bucket&quot;: {
        &quot;buckets_path&quot;: &quot;sales_per_month&gt;sales&quot;,
        &quot;gap_policy&quot;: &quot;skip&quot;,
        &quot;format&quot;: &quot;#,##0.00;(#,##0.00)&quot;
      }
// end::avg-bucket-agg-syntax[]               
    }
  }
}
</code></pre>
<ul>
<li>嵌套的bucket聚合：聚合出按月价格的直方图</li>
<li>Metic聚合：对上面的聚合再求平均值。</li>
</ul>
<p><strong>字段类型</strong>：</p>
<ul>
<li>buckets_path：指定聚合的名称，支持多级嵌套聚合。</li>
<li>gap_policy 当管道聚合遇到不存在的值，有点类似于term等聚合的(missing)时所采取的策略，可选择值为：skip、insert_zeros。</li>
<li>skip：此选项将丢失的数据视为bucket不存在。它将跳过桶并使用下一个可用值继续计算。</li>
<li>format 用于格式化聚合桶的输出(key)。</li>
</ul>
<p>输出结果如下</p>
<pre><code class="language-json">{
  &quot;took&quot;: 11,
  &quot;timed_out&quot;: false,
  &quot;_shards&quot;: ...,
  &quot;hits&quot;: ...,
  &quot;aggregations&quot;: {
    &quot;sales_per_month&quot;: {
      &quot;buckets&quot;: [
        {
          &quot;key_as_string&quot;: &quot;2015/01/01 00:00:00&quot;,
          &quot;key&quot;: 1420070400000,
          &quot;doc_count&quot;: 3,
          &quot;sales&quot;: {
            &quot;value&quot;: 550.0
          }
        },
        {
          &quot;key_as_string&quot;: &quot;2015/02/01 00:00:00&quot;,
          &quot;key&quot;: 1422748800000,
          &quot;doc_count&quot;: 2,
          &quot;sales&quot;: {
            &quot;value&quot;: 60.0
          }
        },
        {
          &quot;key_as_string&quot;: &quot;2015/03/01 00:00:00&quot;,
          &quot;key&quot;: 1425168000000,
          &quot;doc_count&quot;: 2,
          &quot;sales&quot;: {
            &quot;value&quot;: 375.0
          }
        }
      ]
    },
    &quot;avg_monthly_sales&quot;: {
      &quot;value&quot;: 328.33333333333333,
      &quot;value_as_string&quot;: &quot;328.33&quot;
    }
  }
}
</code></pre>
<h3>Stats bucket 聚合</h3>
<p>进一步的stat bucket也很容易理解了</p>
<pre><code class="language-bash">POST /sales/_search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;sales_per_month&quot;: {
      &quot;date_histogram&quot;: {
        &quot;field&quot;: &quot;date&quot;,
        &quot;calendar_interval&quot;: &quot;month&quot;
      },
      &quot;aggs&quot;: {
        &quot;sales&quot;: {
          &quot;sum&quot;: {
            &quot;field&quot;: &quot;price&quot;
          }
        }
      }
    },
    &quot;stats_monthly_sales&quot;: {
      &quot;stats_bucket&quot;: {
        &quot;buckets_path&quot;: &quot;sales_per_month&gt;sales&quot; 
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
   &quot;took&quot;: 11,
   &quot;timed_out&quot;: false,
   &quot;_shards&quot;: ...,
   &quot;hits&quot;: ...,
   &quot;aggregations&quot;: {
      &quot;sales_per_month&quot;: {
         &quot;buckets&quot;: [
            {
               &quot;key_as_string&quot;: &quot;2015/01/01 00:00:00&quot;,
               &quot;key&quot;: 1420070400000,
               &quot;doc_count&quot;: 3,
               &quot;sales&quot;: {
                  &quot;value&quot;: 550.0
               }
            },
            {
               &quot;key_as_string&quot;: &quot;2015/02/01 00:00:00&quot;,
               &quot;key&quot;: 1422748800000,
               &quot;doc_count&quot;: 2,
               &quot;sales&quot;: {
                  &quot;value&quot;: 60.0
               }
            },
            {
               &quot;key_as_string&quot;: &quot;2015/03/01 00:00:00&quot;,
               &quot;key&quot;: 1425168000000,
               &quot;doc_count&quot;: 2,
               &quot;sales&quot;: {
                  &quot;value&quot;: 375.0
               }
            }
         ]
      },
      &quot;stats_monthly_sales&quot;: {
         &quot;count&quot;: 3,
         &quot;min&quot;: 60.0,
         &quot;max&quot;: 550.0,
         &quot;avg&quot;: 328.3333333333333,
         &quot;sum&quot;: 985.0
      }
   }
}
</code></pre>
<h2>参考文章</h2>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-pipeline.html</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43403e6b7070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
