<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>09 查询：DSL查询之Term详解.md</title>
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

                    <a class="current-tab" href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>
                    

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

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
                        <div><h1>09 查询：DSL查询之Term详解</h1>
<h2>Term查询引入</h2>
<p>如前文所述，查询分基于文本查询和基于词项的查询:</p>
<p><img src="assets/es-dsl-full-text-3.png" alt="img" /></p>
<p>本文主要讲基于词项的查询。</p>
<p><img src="assets/es-dsl-term-1.png" alt="img" /></p>
<h2>Term查询</h2>
<blockquote>
<p>很多比较常用，也不难，就是需要结合实例理解。这里综合官方文档的内容，我设计一个测试场景的数据，以覆盖所有例子。@pdai</p>
</blockquote>
<p>准备数据</p>
<pre><code class="language-bash">PUT /test-dsl-term-level
{
  &quot;mappings&quot;: {
    &quot;properties&quot;: {
      &quot;name&quot;: {
        &quot;type&quot;: &quot;keyword&quot;
      },
      &quot;programming_languages&quot;: {
        &quot;type&quot;: &quot;keyword&quot;
      },
      &quot;required_matches&quot;: {
        &quot;type&quot;: &quot;long&quot;
      }
    }
  }
}

POST /test-dsl-term-level/_bulk
{ &quot;index&quot;: { &quot;_id&quot;: 1 }}
{&quot;name&quot;: &quot;Jane Smith&quot;, &quot;programming_languages&quot;: [ &quot;c++&quot;, &quot;java&quot; ], &quot;required_matches&quot;: 2}
{ &quot;index&quot;: { &quot;_id&quot;: 2 }}
{&quot;name&quot;: &quot;Jason Response&quot;, &quot;programming_languages&quot;: [ &quot;java&quot;, &quot;php&quot; ], &quot;required_matches&quot;: 2}
{ &quot;index&quot;: { &quot;_id&quot;: 3 }}
{&quot;name&quot;: &quot;Dave Pdai&quot;, &quot;programming_languages&quot;: [ &quot;java&quot;, &quot;c++&quot;, &quot;php&quot; ], &quot;required_matches&quot;: 3, &quot;remarks&quot;: &quot;hello world&quot;}
</code></pre>
<h3>字段是否存在:exist</h3>
<p>由于多种原因，文档字段的索引值可能不存在：</p>
<ul>
<li>源JSON中的字段是null或[]</li>
<li>该字段已&quot;index&quot; : false在映射中设置</li>
<li>字段值的长度超出ignore_above了映射中的设置</li>
<li>字段值格式错误，并且ignore_malformed已在映射中定义</li>
</ul>
<p>所以exist表示查找是否存在字段。</p>
<p><img src="assets/es-dsl-term-2.png" alt="img" /></p>
<h3>id查询:ids</h3>
<p>ids 即对id查找</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;ids&quot;: {
      &quot;values&quot;: [3, 1]
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-3.png" alt="img" /></p>
<h3>前缀:prefix</h3>
<p>通过前缀查找某个字段</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;prefix&quot;: {
      &quot;name&quot;: {
        &quot;value&quot;: &quot;Jan&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-4.png" alt="img" /></p>
<h3>分词匹配:term</h3>
<p>前文最常见的根据分词查询</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;term&quot;: {
      &quot;programming_languages&quot;: &quot;php&quot;
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-5.png" alt="img" /></p>
<h3>多个分词匹配:terms</h3>
<p>按照读个分词term匹配，它们是or的关系</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;terms&quot;: {
      &quot;programming_languages&quot;: [&quot;php&quot;,&quot;c++&quot;]
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-6.png" alt="img" /></p>
<h3>按某个数字字段分词匹配:term set</h3>
<p>设计这种方式查询的初衷是用文档中的数字字段动态匹配查询满足term的个数</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;terms_set&quot;: {
      &quot;programming_languages&quot;: {
        &quot;terms&quot;: [ &quot;java&quot;, &quot;php&quot; ],
        &quot;minimum_should_match_field&quot;: &quot;required_matches&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-7.png" alt="img" /></p>
<h3>通配符:wildcard</h3>
<p>通配符匹配，比如<code>*</code></p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;wildcard&quot;: {
      &quot;name&quot;: {
        &quot;value&quot;: &quot;D*ai&quot;,
        &quot;boost&quot;: 1.0,
        &quot;rewrite&quot;: &quot;constant_score&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-8.png" alt="img" /></p>
<h3>范围:range</h3>
<p>常常被用在数字或者日期范围的查询</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;range&quot;: {
      &quot;required_matches&quot;: {
        &quot;gte&quot;: 3,
        &quot;lte&quot;: 4
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-9.png" alt="img" /></p>
<h3>正则:regexp</h3>
<p>通过[正则表达式]查询</p>
<p>以&quot;Jan&quot;开头的name字段</p>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;regexp&quot;: {
      &quot;name&quot;: {
        &quot;value&quot;: &quot;Ja.*&quot;,
        &quot;case_insensitive&quot;: true
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-10.png" alt="img" /></p>
<h3>模糊匹配:fuzzy</h3>
<p>官方文档对模糊匹配：编辑距离是将一个术语转换为另一个术语所需的一个字符更改的次数。这些更改可以包括：</p>
<ul>
<li>更改字符（box→ fox）</li>
<li>删除字符（black→ lack）</li>
<li>插入字符（sic→ sick）</li>
<li>转置两个相邻字符（act→ cat）</li>
</ul>
<pre><code class="language-bash">GET /test-dsl-term-level/_search
{
  &quot;query&quot;: {
    &quot;fuzzy&quot;: {
      &quot;remarks&quot;: {
        &quot;value&quot;: &quot;hell&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-term-11.png" alt="img" /></p>
<h2>参考文章</h2>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/term-level-queries.html</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="08&#32;查询：DSL查询之全文搜索详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43402d092e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
