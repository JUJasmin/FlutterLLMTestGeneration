import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:automatic_app_test/paginated_list.dart';


void main() {
  testWidgets('ListView loads more items and shows loading indicator', (WidgetTester tester) async {
    // Build the ListPage widget
    await tester.pumpWidget(MaterialApp(home: ListPage()));

    // Initially, the ListView should display 20 items and a loading indicator
    expect(find.byType(ListTile), findsNWidgets(20));
    expect(find.byType(CircularProgressIndicator), findsOneWidget);

    // Trigger a scroll to the end of the ListView to load more items
    await tester.fling(find.byType(ListView), Offset(0, -500), 3000);
    await tester.pumpAndSettle();

    // After scrolling, the ListView should display 40 items and a loading indicator
    expect(find.byType(ListTile), findsNWidgets(40));
    expect(find.byType(CircularProgressIndicator), findsOneWidget);

    // Trigger another scroll to the end of the ListView to load more items
    await tester.fling(find.byType(ListView), Offset(0, -500), 3000);
    await tester.pumpAndSettle();

    // After the second scroll, the ListView should display 60 items and a loading indicator
    expect(find.byType(ListTile), findsNWidgets(60));
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
  });
}