-- Shared daily stats for the grid games (run once in the Supabase SQL Editor).
-- Tables are locked (row level security, no policies). Visitors can only call the two functions below:
-- record_answer adds a player and a correct answer; grid_stats returns totals, never individual rows.
create table public.plays (
  game text not null,
  grid text not null,
  player uuid not null,
  created_at timestamptz not null default now(),
  primary key (game, grid, player)
);
create table public.answers (
  game text not null,
  grid text not null,
  player uuid not null,
  cell smallint not null check (cell between 0 and 8),
  answer text not null,
  created_at timestamptz not null default now(),
  primary key (game, grid, player, cell)
);
alter table public.plays enable row level security;
alter table public.answers enable row level security;

create function public.record_answer(p_game text, p_grid text, p_player uuid, p_cell int, p_answer text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if length(p_game) > 40 or length(p_grid) > 60 or length(p_answer) > 200 or p_cell not between 0 and 8 then
    raise exception 'bad input';
  end if;
  insert into plays (game, grid, player) values (p_game, p_grid, p_player) on conflict do nothing;
  if p_answer <> '' then
    insert into answers (game, grid, player, cell, answer)
    values (p_game, p_grid, p_player, p_cell, p_answer) on conflict do nothing;
  end if;
end $$;

create function public.grid_stats(p_game text, p_grid text)
returns json language sql stable security definer set search_path = public as $$
  select json_build_object(
    'players', (select count(*) from plays where game = p_game and grid = p_grid),
    'answers', coalesce((
      select json_agg(json_build_object('cell', cell, 'answer', answer, 'n', n))
      from (select cell, answer, count(*) as n from answers
            where game = p_game and grid = p_grid group by cell, answer) t
    ), '[]'::json)
  );
$$;

revoke all on function public.record_answer(text, text, uuid, int, text) from public;
revoke all on function public.grid_stats(text, text) from public;
grant execute on function public.record_answer(text, text, uuid, int, text) to anon;
grant execute on function public.grid_stats(text, text) to anon;
