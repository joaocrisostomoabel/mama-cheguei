#!/usr/bin/env python3
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ── 1. CSS ──────────────────────────────────────────────────────────────────
old_css = '    .test-card cite { font-style: normal; font-size: 0.82rem; color: var(--muted); display: flex; align-items: center; gap: 0.6rem; }'
new_css = old_css + """
    .test-blockquote.is-truncated { display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden; }
    .test-read-more { background: none; border: none; color: var(--crimson); font-size: 0.82rem; cursor: pointer; padding: 0.4rem 0 0; font-family: 'DM Sans', sans-serif; text-decoration: underline; display: block; }"""

if old_css in html:
    html = html.replace(old_css, new_css, 1)
    changes += 1
    print("✅ 1/4  CSS adicionado")
else:
    print("⚠️  1/4  CSS — linha não encontrada (já aplicado?)")

# ── 2. Static HTML testemunhos ───────────────────────────────────────────────
old_grid = """    <div class="test-grid">
      <div class="test-card reveal d1"><div class="test-stars">★★★★★</div><blockquote>"Um sonho tornar-se realidade. Só ela estar lá, tranquila, fez toda a diferença."</blockquote><cite><div class="test-avatar">👶</div>Joana — mãe pela primeira vez</cite></div>
      <div class="test-card reveal d2"><div class="test-stars">★★★★★</div><blockquote>"Pensei que por ser o segundo filho ia ser mais fácil. Não estava nada preparada. Ela chegou e tudo ganhou sentido."</blockquote><cite><div class="test-avatar">🌸</div>Ana — mãe de dois</cite></div>
      <div class="test-card reveal d3"><div class="test-stars">★★★★★</div><blockquote>"Mais do que resolver as dúvidas, fez-me perceber que eu era capaz. Isso foi o maior presente."</blockquote><cite><div class="test-avatar">🤍</div>Mariana — bebé de 6 semanas</cite></div>
    </div>"""

new_grid = """    <div class="test-grid">
      <div class="test-card reveal d1"><div class="test-stars">★★★★★</div><blockquote class="test-blockquote">"Um sonho tornar-se realidade. Só ela estar lá, tranquila, fez toda a diferença."</blockquote><cite><div class="test-avatar">👶</div>Joana — mãe pela primeira vez</cite></div>
      <div class="test-card reveal d2"><div class="test-stars">★★★★★</div><blockquote class="test-blockquote">"Pensei que por ser o segundo filho ia ser mais fácil. Não estava nada preparada. Ela chegou e tudo ganhou sentido."</blockquote><cite><div class="test-avatar">🌸</div>Ana — mãe de dois</cite></div>
      <div class="test-card reveal d3"><div class="test-stars">★★★★★</div><blockquote class="test-blockquote">"Mais do que resolver as dúvidas, fez-me perceber que eu era capaz. Isso foi o maior presente."</blockquote><cite><div class="test-avatar">🤍</div>Mariana — bebé de 6 semanas</cite></div>
      <div class="test-card reveal d1"><div class="test-stars">★★★★★</div><blockquote class="test-blockquote is-truncated">"Tive o privilégio de contar com o acompanhamento da enfermeira Sara no pós-parto, ao domicílio, e não poderia estar mais grata pela experiência. Desde o primeiro momento, demonstrou um elevado profissionalismo, conhecimento técnico e uma enorme sensibilidade no cuidado tanto ao bebé como a mim, enquanto mãe em fase de recuperação. A sua presença trouxe tranquilidade, confiança e segurança num período naturalmente exigente e emocionalmente intenso. Destaco, em particular, a sua disponibilidade, atenção ao detalhe e a forma clara e empática como esclareceu todas as dúvidas, sempre com uma abordagem prática e respeitadora do nosso ritmo enquanto família. Foi, sem dúvida, um apoio fundamental nesta fase tão especial das nossas vidas. Recomendo vivamente os seus serviços a todas as famílias que necessitem de um acompanhamento de excelência, humano e personalizado, no conforto de sua casa."</blockquote><button class="test-read-more" onclick="toggleReadMore(this)">ler mais →</button><cite><div class="test-avatar">💫</div>Ana — mamã do Gabriel (1 mês)</cite></div>
      <div class="test-card reveal d2"><div class="test-stars">★★★★★</div><blockquote class="test-blockquote">"Muito obrigada Sara, você me salvou de uma maneira sem igual. Obrigada pela disponibilidade 🙌🏻 E sim, quando precisar volto a contactar 🫶🏼"</blockquote><cite><div class="test-avatar">🌟</div>Luenda — mãe de um bebé de 5 dias</cite></div>
    </div>"""

if old_grid in html:
    html = html.replace(old_grid, new_grid, 1)
    changes += 1
    print("✅ 2/4  Testemunhos HTML actualizados (5 cards)")
else:
    print("⚠️  2/4  Testemunhos HTML — bloco não encontrado (já aplicado?)")

# ── 3. toggleReadMore function ───────────────────────────────────────────────
old_fn = '  async function loadContent() {'
new_fn = """  function toggleReadMore(btn) {
    const bq = btn.previousElementSibling;
    bq.classList.toggle('is-truncated');
    btn.textContent = bq.classList.contains('is-truncated') ? 'ler mais →' : 'ler menos ↑';
  }

  async function loadContent() {"""

if old_fn in html:
    html = html.replace(old_fn, new_fn, 1)
    changes += 1
    print("✅ 3/4  Função toggleReadMore adicionada")
else:
    print("⚠️  3/4  Função — linha não encontrada (já aplicado?)")

# ── 4. loadContent() testimonials rendering ──────────────────────────────────
old_render = """      const delays = ['', ' d1', ' d2', ' d3'];
        grid.innerHTML = c.testemunhos.map((t, i) =>
          `<div class="test-card reveal visible${delays[i] || ''}">
            <div class="test-stars">★★★★★</div>
            <blockquote>${t.texto}</blockquote>
            <cite><div class="test-avatar">${t.emoji}</div>${t.nome} — ${t.descricao}</cite>
          </div>`
        ).join('');"""

new_render = """      const TRUNC = 200;
        const delays = ['', ' d1', ' d2', ' d3'];
        grid.innerHTML = c.testemunhos.map((t, i) => {
          const isLong = t.texto.length > TRUNC;
          const bqClass = isLong ? ' class="test-blockquote is-truncated"' : ' class="test-blockquote"';
          const btn = isLong ? `<button class="test-read-more" onclick="toggleReadMore(this)">ler mais →</button>` : '';
          return `<div class="test-card reveal visible${delays[i] || ''}">
            <div class="test-stars">★★★★★</div>
            <blockquote${bqClass}>${t.texto}</blockquote>
            ${btn}
            <cite><div class="test-avatar">${t.emoji}</div>${t.nome} — ${t.descricao}</cite>
          </div>`;
        }).join('');"""

if old_render in html:
    html = html.replace(old_render, new_render, 1)
    changes += 1
    print("✅ 4/4  loadContent() testemunhos actualizados")
else:
    print("⚠️  4/4  loadContent() — bloco não encontrado (já aplicado?)")

# ── Write ────────────────────────────────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n🎉 Concluído! {changes}/4 alterações aplicadas.")
print(f"   Ficheiro: index.html ({len(html):,} chars)")
